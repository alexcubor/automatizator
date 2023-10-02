# coding=utf-8
import sys
from .ui import widget_action
from . import widget_attr
from . import code_editor
from . import config
from importlib import reload

reload(widget_action)
reload(widget_attr)
reload(code_editor)
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore


class WidgetAction(QtWidgets.QWidget):
    def __init__(self, parent=None, dictionary=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.ui = widget_action.Ui_widget_action()
        self.ui.setupUi(self)
        self.index = None
        self.dict = dictionary
        self.app_path = config.app_path()
        self.soft = config.soft_name()
        # Name action
        self.ui.title_action.setPlaceholderText(self.dict["title_placeholder"])
        self.ui.title_action.setStyleSheet("background-color: {0}; border: 0px solid {0}".format("#454545"))
        # Bar
        self.ui.button_collapse.setStyleSheet("QPushButton:hover { background-color: %s; }" % config.color_blue())
        self.ui.button_collapse.clicked.connect(self.collapse)
        self.ui.button_mute.setStyleSheet("QPushButton:hover { background-color: %s; }" % config.color_yellow())
        self.ui.button_close.setStyleSheet("QPushButton:hover { background-color: %s; }" % config.color_red())
        # Menu rules
        self.ui.run_menu.setText(self.dict["rule_allways"] + "   ")
        self.ui.menu_run = QtWidgets.QMenu(self.ui.run_menu)
        self.rule_always = self.ui.menu_run.addAction(self.dict["rule_allways"])
        self.rule_always.setProperty("name", "allways")
        self.rule_always.triggered.connect(self.run_by_allways)
        self.rule_scene_path = self.ui.menu_run.addAction(self.dict["rule_scene_path"])
        self.rule_scene_path.setProperty("name", "scene_path")
        self.rule_scene_path.triggered.connect(self.run_by_scene_path)
        self.rule_script = self.ui.menu_run.addAction(self.dict["rule_script"])
        self.rule_script.setProperty("name", "script")
        self.rule_script.triggered.connect(self.run_by_script)
        self.ui.run_menu.setAutoRaise(True)
        self.ui.run_menu.setMenu(self.ui.menu_run)
        self.ui.run_menu.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.ui.run_menu.setProperty("name", "allways")
        self.ui.run_menu.setStyleSheet("border: 0.5px solid {0}".format("#787878"))
        # Hide role objects
        self.ui.run_pattern.setVisible(False)
        # Edit toolbar
        icon = QtGui.QIcon(self.icon("resize.png"))
        self.ui.button_open_script_run.setIcon(icon)
        self.ui.button_open_script_run.setStyleSheet(
            "QPushButton:hover { background-color: %s; }" % config.color_blue())
        self.ui.button_open_script_run.clicked.connect(lambda: code_editor.run(parent=self, plain=self.ui.action_script_run))
        self.ui.button_open_script_run.setVisible(False)
        # Edit
        self.ui.action_script_run.setVisible(False)
        # Menu type
        self.ui.type_menu.setText(self.dict["type_select"] + "   ")
        self.ui.menu_type = QtWidgets.QMenu(self.ui.type_menu)
        self.type_attribute = self.ui.menu_type.addAction(self.dict["type_attr"])
        self.type_attribute.setProperty("name", "attr")
        self.type_attribute.triggered.connect(self.type_by_attr)
        self.type_script = self.ui.menu_type.addAction(self.dict["type_script"])
        self.type_script.setProperty("name", "script")
        self.type_script.triggered.connect(self.type_by_script)
        self.ui.type_menu.setAutoRaise(True)
        self.ui.type_menu.setMenu(self.ui.menu_type)
        self.ui.type_menu.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.ui.type_menu.setProperty("name", "select")
        self.ui.type_menu.setStyleSheet("border: 0.5px solid {0}".format("#787878"))
        # Builder
        icon = QtGui.QIcon(self.icon("resize.png"))
        self.ui.button_open_script_builder.setIcon(icon)
        self.ui.button_open_script_builder.setStyleSheet("QPushButton:hover { background-color: %s; }" % config.color_blue())
        self.ui.button_open_script_builder.clicked.connect(lambda: code_editor.run(parent=self, plain=self.ui.action_script_build))
        # Edit
        self.ui.enable_builder.setText(self.dict["enable_build"])
        self.ui.widget_attr0 = widget_attr.WidgetAttr(parent=self, closer=False)
        self.ui.layout_attrs.addWidget(self.ui.widget_attr0)
        self.ui.enable_builder.setVisible(False)
        self.ui.layout_script_build.addWidget(self.ui.action_script_build)
        self.ui.action_script_build.setPlaceholderText(self.dict["build_placeholder"])
        self.ui.enable_builder.stateChanged.connect(self.enable_builder)
        self.ui.action_script_build.setHidden(
            not self.ui.enable_builder.isChecked() or not self.ui.enable_builder.isVisible())
        self.ui.button_open_script_builder.setHidden(not self.ui.action_script_build.isVisible())
        self.ui.widget_attrs.setHidden(
            not self.ui.enable_builder.isChecked() or not self.ui.enable_builder.isVisible())
        self.ui.action_script_build.setFont(QtGui.QFont("Courier New"))
        self.ui.action_script_build.setTabStopWidth(20)
        self.ui.action_script_build.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        # Checker
        icon = QtGui.QIcon(self.icon("resize.png"))
        self.ui.button_open_script_checker.setIcon(icon)
        self.ui.button_open_script_checker.setStyleSheet(
            "QPushButton:hover { background-color: %s; }" % config.color_blue())
        self.ui.button_open_script_checker.clicked.connect(lambda: code_editor.run(parent=self, plain=self.ui.action_script_check))
        # Edit
        self.ui.enable_checker.setText(self.dict["enable_check"])
        self.ui.action_script_build.setPlaceholderText(self.dict["build_placeholder"])
        self.ui.enable_checker.setVisible(False)
        self.ui.enable_checker.stateChanged.connect(self.enable_checker)
        self.ui.action_script_check.setHidden(
            not self.ui.enable_checker.isChecked() or not self.ui.enable_checker.isVisible())
        self.ui.button_open_script_checker.setHidden(not self.ui.action_script_check.isVisible())
        self.ui.action_script_check.setFont(QtGui.QFont("Courier New"))
        self.ui.action_script_check.setTabStopWidth(20)
        self.ui.action_script_check.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        # Sub actions
        self.ui.menu_override.setVisible(False)
        # Add new action
        self.ui.button_add_override_action.setText(self.dict["add_override"] + " +")
        self.ui.button_add_action.setStyleSheet("QPushButton:hover { background-color: #556B2F; }")

    def enable_builder(self, state):
        self.ui.action_script_build.setHidden(not bool(state))

    def enable_checker(self, state):
        if self.index_menu_action(self.ui.type_menu) == 1:
            self.ui.action_script_check.setHidden(not bool(state))

    # TODO: Почему то не работает
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Tab:
            cursor = self.textCursor()
            cursor.insertText(" " * 4)
            self.setTextCursor(cursor)
        else:
            super().keyPressEvent(event)

    def icon(self, filename):
        return f"{self.app_path}/icons/{filename}"

    def get_action(self, widget=None):
        # TODO: Вспомнить, зачем нужен атрибут widget? Ведь он и не используется, вместо него self.
        if not widget:
            widget = self
        override_data = {}
        # TODO: Оверайды изменили синтаксис и место
        if widget.ui.layout_override_action.children():
            override_widget = widget.ui.layout_override_action.children()[0]
            override_data = self.get_action(override_widget)
        # Base
        data = {"enable": widget.ui.button_mute.isEnabled(),
                "name": widget.ui.title_action.toPlainText(),
                "soft": self.soft,
                "run": widget.ui.run_menu.property("name")
                }
        if data["run"] == "scene_path":
            data["run_scene_path"] = self.ui.run_pattern.text()
        if data["run"] == "script":
            data["run_script"] = self.ui.action_script_run.toPlainText()
        # Override
        data["override"] = override_data
        if override_data:
            data["blend"] = self.ui.menu_override.property("name")
        # Type
        data["type"] = widget.ui.type_menu.property("name")
        if data["type"] == "select":
            data["type"] = None
        # Actions
        if data["type"]:
            data["enable_build"] = widget.ui.enable_builder.isChecked()
            if data["enable_build"]:
                if widget.ui.type_menu.property("name") == "script":
                    data["build_script"] = widget.ui.action_script_build.toPlainText()
                if widget.ui.type_menu.property("name") == "attr":
                    data["attr"] = []
                    for i in range(widget.ui.layout_attrs.count()):
                        item = widget.ui.layout_attrs.itemAt(i).widget()
                        attr = {"type": item.ui.attr_type.text(),
                                "name": item.ui.attr_name.text(),
                                "value": item.ui.attr_value.text()}
                        data["attr"].append(attr)
            data["enable_check"] = widget.ui.enable_checker.isChecked()
            if data["enable_check"]:
                data["check_script"] = widget.ui.action_script_check.toPlainText()
        return data

    def set_action(self, data):
        self.soft = data["soft"]
        self.ui.button_mute.setChecked(data["enable"])
        self.ui.title_action.setText(data["name"])
        if data["run"]:
            self.set_run(data["run"])
            if data["run"] == "scene_path":
                self.ui.run_pattern.setText(data["run_scene_path"])
            if data["run"] == "script":
                self.ui.action_script_run.setPlainText(data["run_script"])
        if data["type"]:
            self.set_type(data["type"])
            self.ui.enable_builder.setChecked(data["enable_build"])
            if data["enable_build"]:
                if data["type"] == "script":
                    self.ui.action_script_build.setPlainText(data["build_script"])
                if data["type"] == "attr":
                    # Remove list attrs
                    for widget in self.ui.layout_attrs.children()[1:]:
                        widget.deleteLater()
                    # Recreate attrs
                    for num, attr in enumerate(data["attr"]):
                        if num == 0:
                            self.ui.widget_attr0.set(type=attr["type"], attr=attr["name"], value=attr["value"])
                        else:
                            widget = widget_attr.WidgetAttr(parent=self, adder=False)
                            widget.set(type=attr["type"], attr=attr["name"], value=attr["value"])
                            self.ui.layout_attrs.addWidget(widget)
            self.ui.enable_checker.setChecked(data["enable_check"])
            if data["enable_check"]:
                if data["type"] == "script":
                    self.ui.action_script_check.setPlainText(data["check_script"])

    @staticmethod
    def index_menu_action(tool_menu):
        for index, action in enumerate(tool_menu.menu().actions()):
            if action.text() in tool_menu.text():
                return index

    def run_by_allways(self):
        self.ui.run_menu.setText(self.dict["rule_allways"] + "   ")
        self.ui.run_menu.setProperty("name", "allways")
        self.ui.run_pattern.setVisible(False)
        self.ui.action_script_run.setVisible(False)

    def run_by_scene_path(self):
        self.ui.run_menu.setText(self.dict["rule_scene_path"] + "   ")
        self.ui.run_menu.setProperty("name", "scene_path")
        self.ui.run_pattern.setVisible(True)
        self.ui.action_script_run.setVisible(False)

    def run_by_script(self):
        self.ui.run_menu.setText(self.dict["rule_script"] + "   ")
        self.ui.run_menu.setProperty("name", "script")
        self.ui.run_pattern.setVisible(False)
        self.ui.action_script_run.setVisible(True)

    def set_run(self, run_name):
        if run_name == "allways":
            self.run_by_allways()
        if run_name == "scene_path":
            self.run_by_scene_path()
        if run_name == "script":
            self.run_by_script()

    def type_by_attr(self):
        self.ui.enable_checker.setVisible(True)
        self.ui.button_open_script_checker.setVisible(False)
        self.ui.action_script_check.setVisible(False)
        self.ui.enable_builder.setVisible(True)
        self.ui.widget_attrs.setVisible(True)
        self.ui.button_open_script_checker.setVisible(False)
        self.ui.action_script_build.setVisible(False)
        self.ui.type_menu.setText(self.dict["type_attr"] + "   ")
        self.ui.type_menu.setProperty("name", "attr")

    def type_by_script(self):
        self.ui.enable_checker.setVisible(True)
        self.ui.button_open_script_builder.setVisible(True)
        self.ui.action_script_build.setVisible(True)
        self.ui.enable_builder.setVisible(True)
        self.ui.widget_attrs.setVisible(False)
        self.ui.button_open_script_checker.setVisible(True)
        self.ui.action_script_check.setVisible(True)
        self.ui.type_menu.setText(self.dict["type_script"] + "   ")
        self.ui.type_menu.setProperty("name", "script")

    def set_type(self, type_name):
        if type_name == "attr":
            self.type_by_attr()
        if type_name == "script":
            self.type_by_script()

    def collapse(self):
        if self.ui.frame_action.isVisible():
            self.ui.frame_action.setVisible(False)
            self.ui.button_mute.setVisible(False)
            self.ui.button_close.setVisible(False)
            self.ui.button_collapse.setText(">")
            self.setMaximumHeight(70)
        else:
            self.ui.frame_action.setVisible(True)
            self.ui.button_mute.setVisible(True)
            self.ui.button_close.setVisible(True)
            self.ui.button_collapse.setText("v")
            self.setMaximumHeight(1000)
