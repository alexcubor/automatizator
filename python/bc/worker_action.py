# coding=utf-8
from .ui import worker_action
from . import config
from importlib import reload

reload(worker_action)
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore


class WorkerAction(QtWidgets.QWidget):
    def __init__(self, parent=None, dictionary=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.ui = worker_action.Ui_Form()
        self.ui.setupUi(self)

    def update_status(self, progress_value, result, message):
        if result == "True":
            status_done = QtGui.QPixmap(f"{self.parent.app_path}/icons/status_done.png")
            self.ui.status.setPixmap(status_done)
            self.ui.info.setVisible(False)
            self.ui.fix_button.setVisible(False)
        elif result == "False":
            status_error = QtGui.QPixmap(f"{self.parent.app_path}/icons/status_error.png")
            self.ui.status.setPixmap(status_error)
            if message:
                self.ui.info.setVisible(True)
                self.ui.info.setPlainText(message)
            font_metrics = QtGui.QFontMetrics(self.ui.info.font())
            text_size = font_metrics.size(QtCore.Qt.TextSingleLine, self.ui.info.toPlainText())
            if text_size.height() == 0:
                self.ui.info.setVisible(False)
            if text_size.height() < 100:
                self.ui.info.setMaximumSize(1000, text_size.height() + 13)
                self.ui.info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        else:
            status_warning = QtGui.QPixmap(f"{self.parent.app_path}/icons/status_warning.png")
            self.ui.status.setPixmap(status_warning)
            if message:
                self.ui.info.setVisible(True)
                self.ui.info.setPlainText(message)
                font_metrics = QtGui.QFontMetrics(self.ui.info.font())
                text_size = font_metrics.size(QtCore.Qt.TextSingleLine, self.ui.info.toPlainText())
                if text_size.height() == 0:
                    self.ui.info.setVisible(False)
                if text_size.height() < 100:
                    self.ui.info.setMaximumSize(1000, text_size.height() + 13)
                    self.ui.info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.parent.ui.progress_bar.setValue(progress_value)
