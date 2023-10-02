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
