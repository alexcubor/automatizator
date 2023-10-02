# coding=utf-8
import sys
from .ui import code_editor
from . import config
from importlib import reload

reload(config)
from PySide2 import QtWidgets
from PySide2 import QtGui


class CodeEditor(QtWidgets.QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.dict = config.get_dictionary()
        self.setWindowTitle(self.dict["code_editor"])
        self.plain = None
        self.ui = code_editor.Ui_CodeEditor()
        self.ui.setupUi(self)
        self.dict = config.get_dictionary()
        self.app_path = config.app_path()
        self.soft = config.soft_name()

        self.ui.edit_code.setFont(QtGui.QFont("Courier New"))
        self.ui.edit_code.setTabStopWidth(20)
        self.ui.edit_code.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.ui.edit_code.cursorPositionChanged.connect(self.update_label)

        self.ui.button_apply.setText(self.dict["apply"])
        self.ui.button_apply.clicked.connect(self.apply)
        self.ui.button_accept.setText(self.dict["accept"])
        self.ui.button_accept.clicked.connect(self.accept)
        self.ui.button_close.setText(self.dict["close"])
        self.ui.button_close.clicked.connect(self.close)

    def update_label(self):
        cursor = self.ui.edit_code.textCursor()
        line = cursor.blockNumber() + 1
        column = cursor.columnNumber() + 1
        self.ui.call_line.setText(f"Ln {line} | Col {column}")

    def apply(self):
        self.plain.setPlainText(self.ui.edit_code.toPlainText())

    def accept(self):
        self.apply()
        self.close()


def run(dev=False, parent=None, plain=None):
    dialog = CodeEditor(parent=parent)
    dialog.plain = plain
    dialog.ui.edit_code.setPlainText(plain.toPlainText())
    dialog.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dialog = CodeEditor()
    dialog.exec_()
