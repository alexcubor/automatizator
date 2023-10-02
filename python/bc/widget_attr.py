from PySide2 import QtWidgets
from .ui import widget_attr
from importlib import reload
reload(widget_attr)


class WidgetAttr(QtWidgets.QWidget):
    def __init__(self, parent=None, adder=True, closer=True, *args, **kwargs):
        super().__init__(parent, *args, *kwargs)
        self.parent = parent
        self.ui = widget_attr.Ui_Form()
        self.ui.setupUi(self)
        self.id = self.parent.ui.layout_attrs.count() + 1
        # Add
        self.ui.attr_button_add.setStyleSheet("QPushButton:hover { background-color: #556B2F; }")
        self.ui.attr_button_add.clicked.connect(self.add)
        # Close
        self.ui.attr_close.setStyleSheet("background-color: #8e4646;")
        self.ui.attr_close.clicked.connect(self.deleteLater)
        if not adder:
            self.ui.attr_button_add.deleteLater()
        if not closer:
            self.ui.attr_close.deleteLater()

    def add(self):
        self.parent.ui.layout_attrs.addWidget(WidgetAttr(parent=self.parent, adder=False))

    def set(self, type=None, attr=None, value=None):
        if type:
            self.ui.attr_type.setText(str(type))
        if attr:
            self.ui.attr_name.setText(str(attr))
        if value:
            self.ui.attr_value.setText(str(value))
