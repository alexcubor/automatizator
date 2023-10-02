# coding=utf-8
import sys
from .ui import widget_button
from . import code_editor
from . import config
from importlib import reload

reload(widget_button)
reload(code_editor)
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore


class WidgetButton(QtWidgets.QWidget):
    def __init__(self, parent=None, dictionary=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.ui = widget_button.Ui_Form()
        self.ui.setupUi(self)
        self.index = None
        self.dict = dictionary
        self.app_path = config.app_path()
        self.soft = config.soft_name()

        self.ui.button_script.setPlaceholderText(self.dict["button_placeholder"])
        self.ui.button_script.setFont(QtGui.QFont("Courier New"))
        self.ui.button_script.setTabStopWidth(20)
        self.ui.button_script.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)

    # TODO: Почему то не работает
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Tab:
            cursor = self.textCursor()
            cursor.insertText(" " * 4)
            self.setTextCursor(cursor)
        else:
            super().keyPressEvent(event)

    def get_button(self):
        data = {"name": self.ui.button_name.toPlainText(),
                "script": self.ui.button_script.toPlainText(),
                }
        return data

    def set_action(self, data):
        self.soft = data["soft"]
        self.ui.button_name.setText(data["name"])
        self.ui.button_script.setPlainText(data["name"])
