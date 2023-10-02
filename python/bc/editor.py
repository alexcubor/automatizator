import os
import re
from PySide2 import QtWidgets, QtGui, QtCore
import configparser
import subprocess
from . import config

import json

from .ui import dialog
from . import widget_action
from . import dialog_save_shelf
from importlib import reload

reload(widget_action)
reload(dialog)
reload(dialog_save_shelf)
reload(config)


class Editor(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        self.name = config.name()
        self.app_path = config.app_path()
        self.ui = dialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.dict = config.get_dictionary()
        self.setWindowTitle(f"{self.dict['app_name']} - {self.dict['editor']}")
        self.default_file = config.preference_dir() + "/actions.actn"
        # self.setWindowFlags(self.windowFlags() | QtGui.Qt.WindowMinimizeButtonHint)
        self.bg_color = self.palette().color(QtGui.QPalette.Base).name()
        # Menu File
        submenu_file = QtWidgets.QMenu(self.ui.menu_file)
        self.file_new = submenu_file.addAction(self.dict["new"])
        self.file_new.triggered.connect(self.new_actions)
        self.file_open_menu = submenu_file.addMenu(self.dict["menu_open"])
        self.file_open_file = self.file_open_menu.addAction(self.dict["open_file"])
        self.file_open_file.triggered.connect(self.open_file)
        self.file_open_sep = self.file_open_menu.addSeparator()
        for worker_path in self.shelf_workers():
            shelf_button = self.file_open_menu.addAction("Shelf " + os.path.splitext(os.path.basename(worker_path))[0])
            shelf_button.triggered.connect(lambda: self.load_actions(file_actions=worker_path))
        self.resent_sep = self.file_open_menu.addSeparator()
        for recent_file in config.get_recent()[-5:]:
            if recent_file:
                text = recent_file[-50:] if len(recent_file) < 51 else "..." + recent_file[-50:]
                recent_button = self.file_open_menu.addAction(text)
                static_path = recent_file
                recent_button.triggered.connect(lambda: self.load_actions(file_actions=static_path))
        self.file_import = submenu_file.addAction(self.dict["import"])
        self.file_save = submenu_file.addAction(self.dict["save"])
        self.file_save.triggered.connect(lambda: self.save_file(force=True))
        self.file_save.setShortcut(QtGui.QKeySequence("Ctrl+S"))
        self.file_save_to_shelf = submenu_file.addAction(self.dict["save_to_shelf"])
        self.file_save_to_shelf.triggered.connect(lambda: dialog_save_shelf.run(parent=self))
        self.file_save_as = submenu_file.addAction(self.dict["save_to_file"])
        self.file_save_as.triggered.connect(self.save_file)
        self.ui.menu_file.setAutoRaise(True)
        self.ui.menu_file.setMenu(submenu_file)
        self.ui.menu_file.setText(self.dict["file"])
        self.ui.menu_file.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        # Menu Settings
        menu_settings = QtWidgets.QMenu(self.ui.menu_settings)
        self.menu_lang = menu_settings.addMenu(self.dict["lang"])
        self.lang_ru = self.menu_lang.addAction("Русский")
        self.lang_ru.triggered.connect(lambda set_lang_ru: self.set_lang("ru"))
        self.lang_en = self.menu_lang.addAction("English")
        self.lang_en.triggered.connect(lambda set_lang_en: self.set_lang("en"))
        self.ui.menu_settings.setAutoRaise(True)
        self.ui.menu_settings.setMenu(menu_settings)
        self.ui.menu_settings.setText(self.dict["settings"])
        self.ui.menu_settings.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        # Menu Help
        menu_help = QtWidgets.QMenu(self.ui.menu_help)
        self.help_start = menu_help.addAction(self.dict["get_start"])
        # For translate example name in menu
        # subprocess.check_output(f'xattr -w ru "Изменение параметров" "{self.app_path}/examples/Change parameters.actn"', shell=True)
        if os.path.isdir(self.app_path + f"/examples/{config.soft_name()}"):
            self.ui.menu_examples = menu_help.addMenu(self.dict["examples"])
            for file_action in os.listdir(self.app_path + f"/examples/{config.soft_name()}"):
                if file_action.endswith(".actn"):
                    # TODO: Разобраться почему triggered.connect везде меняет путь на последний в списке?
                    #  Пока оставил только один пример.
                    if "Assembly scene" not in file_action:
                        continue
                    action_path = self.app_path + f"/examples/{config.soft_name()}/" + file_action
                    name = file_action.rsplit(".", 1)[0]
                    label = name
                    try:
                        label = subprocess.check_output(f'xattr -p {config.get_language()} "{action_path}"',
                                                        shell=True).decode("utf-8").replace("\n", "")
                    except:
                        pass
                    static_path = self.app_path + f"/examples/{config.soft_name()}/{label}.actn"
                    action_example = self.ui.menu_examples.addAction(name)
                    action_example.triggered.connect(lambda: self.load_actions(file_actions=static_path))
        self.help_about = menu_help.addAction(self.dict["about"])
        self.ui.menu_help.setAutoRaise(True)
        self.ui.menu_help.setMenu(menu_help)
        self.ui.menu_help.setText(self.dict["help"])
        self.ui.menu_help.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        # Add new action
        self.ui.button_add_action0.clicked.connect(lambda: self.insert_widget_action(1))
        self.ui.button_add_action0.setStyleSheet("QPushButton:hover { background-color: %s; }" % config.color_green())
        # List actions
        self.opened_file = config.get_recent()[0]
        self.load_actions(file_actions=self.opened_file, force=True)
        self.update_indexes()
        # Checker buttons
        self.ui.buttons_info.setText(self.dict["buttons_info"])

    def widget_action(self):
        widget = widget_action.WidgetAction(parent=self, dictionary=self.dict)
        widget.ui.button_add_action.clicked.connect(lambda: self.insert_widget_action(widget.index + 1))
        widget.ui.button_close.clicked.connect(lambda: self.delete_widget(widget))
        return widget

    def delete_widget(self, widget):
        self.ui.layout_tabs.removeWidget(widget)
        widget.deleteLater()
        self.update_indexes()

    def insert_widget_action(self, index):
        self.ui.layout_tabs.insertWidget(index, self.widget_action())
        self.update_indexes()

    # Menu functions
    def open_file(self):
        # Open a file dialog to select a file to open
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "",
                                                             "Action Files (*.actn);;All Files (*)")
        if file_name:
            self.load_actions(file_actions=file_name)

    def shelf_workers(self):
        buttons = []
        if config.soft_name() == "maya":
            import maya.cmds as cmds
            for button in cmds.shelfLayout(self.name, q=True, childArray=True):
                script = cmds.shelfButton(button, q=True, command=True)
                match = re.search(r'worker\.run\(file="(.+)",', script)
                if match:
                    path = match.group(1)
                    if path not in buttons:
                        buttons.append(path)
        return buttons

    def save_file(self, force=False):
        # Open a file dialog to select a file to save to
        if not force:
            self.opened_file, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File",
                                                                        self.opened_file.split('/')[-1],
                                                                        "Action Files (*.actn);;All Files (*)")
        if self.opened_file:
            # Save the contents of a text editor to the selected file
            self.save(self.current_actions())
        self.update_title()

    def save(self, data):
        with open(self.opened_file, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        file.close()

    def save_to_shelf(self, name):
        shelf_folder = config.preference_dir() + "/buttons"
        if not os.path.isdir(shelf_folder):
            os.makedirs(shelf_folder)
        file_actions = f"{shelf_folder}/{name}.actn"
        actions = self.current_actions()["action"]["main_actions"]
        is_build = True if True in [a["enable_build"] for a in actions if "enable_build" in a] else False
        is_check = True if True in [a["enable_check"] for a in actions if "enable_check" in a] else False
        if not is_build and not is_check:
            is_build = True
            is_check = True
        self.opened_file = file_actions
        self.save(actions)
        if name not in self.shelf_workers():
            if config.soft_name() == "maya":
                import maya.cmds as cmds
                if is_build:
                    command = 'from bc import worker; from importlib import reload; reload(worker); worker.run(' \
                              'file="%s", mode="build")' % file_actions
                    cmds.shelfButton(parent=self.name, label=name, iol=name, command=command, image="bc_build.png")
                if is_check:
                    command = 'from bc import worker; from importlib import reload; reload(worker); worker.run(' \
                              'file="%s", mode="check")' % file_actions
                    cmds.shelfButton(parent=self.name, label=name, iol=name, command=command, image="bc_check.png")
        self.opened_file = file_actions

    def set_lang(self, lang):
        config_pars = configparser.ConfigParser()
        file_lang = config.preference_path()
        config_pars.read(file_lang)
        config_pars.set("LOCALE", "language", lang)
        with open(file_lang, "w") as configfile:  # Save prefs
            config_pars.write(configfile)
        self.dict = config.get_dictionary()
        self.setWindowTitle(f"{self.dict['app_name']} - {self.dict['editor']}")
        self.ui.menu_file.setText(self.dict["file"])
        self.file_new.setText(self.dict["new"])
        self.file_open_file.setText(self.dict["open_file"])
        self.file_import.setText(self.dict["import"])
        self.file_save.setText(self.dict["save"])
        self.ui.menu_settings.setText(self.dict["settings"])
        self.menu_lang.setTitle(self.dict["lang"])
        self.ui.menu_help.setText(self.dict["help"])
        self.help_about.setText(self.dict["about"])
        self.help_start.setText(self.dict["get_start"])
        for i in range(self.ui.layout_tabs.count() - 1):
            action_widget = self.ui.layout_tabs.itemAt(i).widget()
            rule_name = "rule_" + action_widget.ui.run_menu.property("name")
            action_widget.ui.run_menu.setText(self.dict[rule_name] + "   ")
            for action in [action_widget.rule_always, action_widget.rule_scene_path, action_widget.rule_script]:
                action_name = action.property("name")
                action.setText(self.dict["rule_" + action_name])
            action_widget.ui.enable_builder.setText(self.dict["enable_build"])
            type_name = "type_" + action_widget.ui.type_menu.property("name")
            action_widget.ui.type_menu.setText(self.dict[type_name] + "   ")
            for action in [action_widget.type_attribute, action_widget.type_script]:
                action_name = action.property("name")
                action.setText(self.dict["type_" + action_name])
            action_widget.ui.enable_checker.setText(self.dict["enable_check"])
        for i in range(self.ui.layout_buttons.count() - 1):
            button_widget = self.ui.layout_buttons.itemAt(i).widget()
            button_widget.ui.button_script.setPlaceholderText(self.dict["button_placeholder"])

    def new_actions(self):
        actions = config.default_actions()
        result = self.check_changes()
        if result == False:
            return
        self.update_ui(actions, file_actions=self.opened_file)

    def load_actions(self, file_actions=None, force=False):
        def _create_default_actions():
            self.opened_file = self.default_file
            actions = config.default_actions()
            self.save(actions)
            return self.opened_file

        if not file_actions:
            if not os.path.isfile(file_actions):
                file_actions = _create_default_actions()
        if not os.path.isfile(file_actions):
            file_actions = _create_default_actions()

        with open(file_actions, "r") as file:  # Open local actions
            actions = json.load(file)
        # Check by changes?
        if not force:
            result = self.check_changes()
            if result == False:
                return
        print('update_ui', file_actions)
        self.update_ui(actions, file_actions=file_actions)

    def update_ui(self, data, file_actions=None):
        # Clean actions before
        for index in range(self.ui.layout_tabs.count()):
            widget = self.ui.layout_tabs.itemAt(0).widget()
            self.delete_widget(widget)
        # Add actions
        try:
            last_output = list(data["output"].keys())[-1]
            main_actions = data["output"][last_output]["actions"]
            actions = data["action"][main_actions]
        except:
            # TODO: Убрать. Оставить только то, что в try
            actions = data
        for action in actions:
            height = 0
            if action["soft"] == config.soft_name() or not action["soft"]:
                widget = self.widget_action()
                widget.set_action(action)
                self.ui.layout_tabs.insertWidget(self.ui.layout_tabs.count(), widget)
                height += widget.height()
            self.resize(self.width(), height)
        if not self.app_path + "/examples/" in file_actions:
            self.opened_file = file_actions
        else:
            self.opened_file = self.default_file
        self.update_title()
        self.update_indexes()

    def update_indexes(self):
        for index in range(self.ui.layout_tabs.count()):
            widget = self.ui.layout_tabs.itemAt(index).widget()
            widget.index = index

    def update_title(self):
        if self.opened_file != self.default_file:
            self.setWindowTitle(f"{self.name} - {self.opened_file.split('/')[-1]}")

    def current_actions(self):
        actions = []
        count_actions = self.ui.layout_tabs.count()
        for index in range(count_actions):
            item = self.ui.layout_tabs.itemAt(index).widget()
            action = item.get_action()
            actions.append(action)
        buttons = []
        count_buttons = self.ui.layout_buttons.count()
        for index in range(count_buttons):
            item = self.ui.layout_tabs.itemAt(index).widget()
            button = item.get_button()
            buttons.append(button)
        data = {"info": {"version": config.version()},
                "action": {"main_actions": actions},
                "button": {"main_buttons": buttons},
                "output": {"output_actions": {"actions": "main_actions", "buttons": "main_buttons"}}}
        return data

    def current_file_actions(self):
        with open(self.opened_file, "r") as file:  # Open local actions
            actions = json.load(file)
            #try:
            #    last_output = data["output"].keys()[-1]
            #    main_actions = data["output"][last_output]["actions"]
            #    actions = data["action"][main_actions]
            #except:
            #    # TODO: Убрать. Оставить только то, что в try
            #    return actions
            return actions

    def check_changes(self):
        if self.current_file_actions() == self.current_actions():
            return True
        # Show a warning message box
        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Warning)
        message_box.setWindowTitle(self.dict["warning"])
        message_box.setText(self.dict["wrn_changes_message"])
        message_box.setStandardButtons(
            QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)
        message_box.setDefaultButton(QtWidgets.QMessageBox.Save)
        response = message_box.exec()
        if response == QtWidgets.QMessageBox.Save:
            file_actions = self.opened_file
            if f"{self.app_path}/examples/" in file_actions:
                file_actions = self.default_file
            self.save(file_actions)
            return True
        elif response == QtWidgets.QMessageBox.Discard:
            pass
        else:
            return False

    def closeEvent(self, event):
        if self.opened_file != self.default_file and self.opened_file not in config.get_recent():
            config_pars = configparser.ConfigParser()
            file_pref = config.preference_path()
            config_pars.read(file_pref)
            config_pars.set("LOCALE", "recent6", config_pars.get("LOCALE", "recent5"))
            config_pars.set("LOCALE", "recent5", config_pars.get("LOCALE", "recent4"))
            config_pars.set("LOCALE", "recent4", config_pars.get("LOCALE", "recent3"))
            config_pars.set("LOCALE", "recent3", config_pars.get("LOCALE", "recent2"))
            config_pars.set("LOCALE", "recent2", config_pars.get("LOCALE", "recent1"))
            config_pars.set("LOCALE", "recent1", self.opened_file)
            with open(file_pref, "w") as configfile:  # Save prefs
                config_pars.write(configfile)
        action_files = [x.split(".")[0] for x in os.listdir(config.preference_dir() + "/buttons")]
        for action_file in action_files:
            if action_file not in self.shelf_workers():
                action_path = f"{config.preference_dir()}/buttons/{action_file}.actn"
                if os.path.isfile(action_path):
                    # TODO: Почему то удаляет даже то, что не должно удаляться.
                    print("WILL REMOVE", action_file)
                    #os.remove(action_path)

        result = self.check_changes()
        if result == False:
            event.ignore()
        else:
            event.accept()


def run(dev=False):
    parent = None
    if config.soft_name() == "maya":
        from maya import OpenMayaUI
        import shiboken2 as shiboken
        main_windows = OpenMayaUI.MQtUtil.mainWindow()
        parent = shiboken.wrapInstance(int(main_windows), QtWidgets.QWidget)
    dialog = Editor(parent=parent)
    dialog.show()
    # dialog.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dialog = Editor()
    dialog.exec_()
