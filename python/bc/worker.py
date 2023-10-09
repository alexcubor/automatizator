import sys

from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
import traceback
from . import config
from importlib import reload
import inspect
import json
import time

from .ui import worker
from . import worker_action

reload(config)
reload(worker)
reload(worker_action)


class Worker(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.dict = config.get_dictionary()
        self.app_path = config.app_path()
        self.file = None
        self.mode = None
        self.result = True
        self.ui = worker.Ui_Dialog()
        self.ui.setupUi(self)
        self.last_widget = None

    def start(self):
        with open(self.file, "r") as file:
            data = json.load(file)
        actions = data["action"]["main_actions"]
        if self.mode == "check":
            buttons = data["button"]["main_buttons"]
            # Post button
            for button_data in buttons:
                button = QtWidgets.QPushButton(button_data["name"])
                button.clicked.connect(lambda: exec(button_data["script"]))
                self.ui.post_buttons.addWidget(button)
        # Create an instance of the ProgressThread
        thread = ProgressThread(self)
        thread.mode = self.mode
        thread.actions = actions
        # Connect the progress_updated signal to update the progress bar
        thread.progress_start.connect(self.add_step)
        thread.progress_updated.connect(self.update_status)
        thread.change_fix_button.connect(self.add_fix_button)
        thread.progress_done.connect(self.finish)
        thread.start()
        # Run button
        if self.result == True:
            for index in range(self.ui.post_buttons.count()):
                post_button = self.ui.post_buttons.itemAt(index).widget()
                result, message = post_button.click()
                label_message = QtWidgets.QLabel(message)
                self.ui.post_buttons.addWidget(label_message)

    def add_step(self, action_name):
        widget = worker_action.WorkerAction(parent=self, dictionary=self.dict)
        widget.ui.action_name.setText(action_name)
        widget.ui.info.setVisible(False)
        widget.ui.fix_button.setVisible(False)
        widget.ui.fix_button.setText(self.dict["fix"])
        status_progress = QtGui.QMovie(self.app_path + "/icons/status_progress.webp")
        widget.ui.status.setMovie(status_progress)
        status_progress.start()
        self.ui.scroll_layout.addWidget(widget)
        scroll_bar = self.ui.scroll_area.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())
        self.last_widget = widget
        sep_line = QtWidgets.QFrame(frameShape=QtWidgets.QFrame.HLine, frameShadow=QtWidgets.QFrame.Sunken)
        self.ui.scroll_layout.addWidget(sep_line)

    def update_status(self, progress_value, result, message):
        if result == "True":
            status_done = QtGui.QPixmap(f"{self.app_path}/icons/status_done.png")
            self.last_widget.ui.status.setPixmap(status_done)
        elif result == "False":
            status_error = QtGui.QPixmap(f"{self.app_path}/icons/status_error.png")
            self.result = False
            self.last_widget.ui.status.setPixmap(status_error)
            if message:
                self.last_widget.ui.info.setVisible(True)
                self.last_widget.ui.info.setPlainText(message)
            font_metrics = QtGui.QFontMetrics(self.last_widget.ui.info.font())
            text_size = font_metrics.size(QtCore.Qt.TextSingleLine, self.last_widget.ui.info.toPlainText())
            if text_size.width() == 0:
                self.last_widget.ui.info.setVisible(False)
            if text_size.width() < 100:
                self.last_widget.ui.info.setMaximumSize(1000, text_size.width())
                self.last_widget.ui.info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        else:
            status_warning = QtGui.QPixmap(f"{self.app_path}/icons/status_warning.png")
            if self.result != False:
                self.result = "warning"
            self.last_widget.ui.status.setPixmap(status_warning)
            if message:
                self.last_widget.ui.info.setVisible(True)
                self.last_widget.ui.info.setPlainText(message)
                font_metrics = QtGui.QFontMetrics(self.last_widget.ui.info.font())
                text_size = font_metrics.size(QtCore.Qt.TextSingleLine, self.last_widget.ui.info.toPlainText())
                if text_size.width() == 0:
                    self.last_widget.ui.info.setVisible(False)
                if text_size.width() < 100:
                    self.last_widget.ui.info.setMaximumSize(1000, text_size.width())
                    self.last_widget.ui.info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ui.progress_bar.setValue(progress_value)

    def add_fix_button(self, visible, name, script):
        if self.mode == "check" and visible:
            self.last_widget.ui.fix_button.setVisible(True)
            if name:
                self.last_widget.ui.fix_button.setText(name)
            self.last_widget.ui.fix_button.clicked.connect(lambda: exec(script))

    def finish(self):
        label_done = QtWidgets.QLabel(self.dict["build_done"])
        label_done.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.verticalLayout.addWidget(label_done)


class ProgressThread(QtCore.QThread):
    progress_start = QtCore.Signal(str)
    progress_updated = QtCore.Signal(int, str, str)
    progress_done = QtCore.Signal(str)
    change_fix_button = QtCore.Signal(bool, str, str)

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.mode = None
        self.actions = None

    def run(self):
        for action in self.actions:
            if not action["type"]:
                self.actions.remove(action)
            else:
                if not action[f"enable_{self.mode}"]:
                    self.actions.remove(action)
        for i, action in enumerate(self.actions):
            self.progress_start.emit(action["name"])
            # Simulate work being done
            time.sleep(0.01)
            # Run script
            result, message = None, None
            if action["type"] == "script":
                def fix_button(visible=True, name=None, script=None):
                    if not script:
                        out_build_script = "    " + action['build_script'].replace('\n', '\n    ')
                        script = f"def build_script():    \n{out_build_script}\nresult = build_script()"
                    return self.change_fix_button.emit(visible, name, script)

                out_script = action[f'{self.mode}_script']
                if out_script:
                    out_script = "    " + out_script.replace('\n', '\n    ')
                    run_script = f"def build_script():    \n{out_script}\nresult = build_script()"
                    try:
                        local_vars = {}
                        global_vars = {}
                        exec(run_script, global_vars, local_vars)
                        if type(local_vars.get("result")) == tuple:
                            result, message = local_vars.get("result")
                        else:
                            result, message = local_vars.get("result"), None
                    except Exception as e:
                        print("---------------")
                        print(f"Exec [{i + 1} {action['name']}] Error", str(e))
                        for num, line in enumerate(run_script.split("\n")):
                            print(line)
                        print("---Traceback---")
                        print(traceback.format_exc())
                        print("---------------")
                        result, message = False, e
            if action["type"] == "attr":
                if config.soft_name() == "maya":
                    import maya.cmds as cmds
                    for num_attr_group, attr_group in enumerate(action["attr"]):
                        attrs = cmds.ls(attr_group['name'])
                        if not attrs:
                            result = False
                            break

                        for num_attr, attr in enumerate(attrs):
                            if attr_group["type"]:
                                node = attr.split(".")[0]
                                if cmds.nodeType(node) != attr_group["type"]:
                                    continue
                            type_attr = cmds.getAttr(attr, type=True)
                            value = attr_group['value']
                            script = None
                            if type_attr == "doubleLinear" or type_attr == "long":
                                script = f"cmds.setAttr('{attr}', float({value}))"
                            if type_attr == "float3":
                                value = value.replace(", ", " ").replace(",", " ")
                                value = [float(x) for x in value.split()]
                                script = f"cmds.setAttr('{attr}', {value[0]}, {value[1]}, {value[2]})"
                            try:
                                local_vars = {}
                                global_vars = {}
                                script = "import maya.cmds as cmds;" + script
                                exec(script, global_vars, local_vars)
                                result, message = True, None
                            except Exception as e:
                                for num, line in enumerate(script.split("\n")):
                                    print([num], line)
                                print("---------------")
                                print(f"Exec [{i}] Error:", str(e))
                                result, message = False, e
            self.progress_updated.emit(int(100 / len(self.actions) * (i + 1)), str(result), message)
        self.progress_done.emit("")

    def close(self):
        self.finished.emit()


def run(file=None, mode=None):
    parent = None
    if config.soft_name() == "maya":
        from maya import OpenMayaUI
        import shiboken2 as shiboken
        main_windows = OpenMayaUI.MQtUtil.mainWindow()
        parent = shiboken.wrapInstance(int(main_windows), QtWidgets.QWidget)

    # Create the main dialog
    app = QtWidgets.QApplication.instance()
    dialog = Worker(parent=parent)
    dialog.file = file
    dialog.mode = mode
    dialog.setWindowTitle(f"{dialog.dict['app_name']} — {dialog.dict[dialog.mode + 'er']}")
    dialog.show()
    dialog.start()
    # Start the event loop
    app.exec_()
