import os

from . import config
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QFont
from PySide2.QtWidgets import QPushButton, QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy


class SaveShelf(QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.app_path = config.app_path()
        self.dict = config.get_dictionary()
        self.setWindowTitle(self.dict["save_to_shelf_title"])
        self.setFixedSize(230, 160)
        layout = QGridLayout()
        self.setLayout(layout)
        # Create and set the icon picture
        icon_label = QLabel(self)
        icon_pixmap = QPixmap(self.app_path + "/icons/bc_build.png").scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(icon_pixmap)
        layout.addWidget(icon_label, 0, 0, 1, 1)
        icon_label.setAlignment(Qt.AlignCenter)
        # Create the editable text field
        self.text_edit = QLineEdit(self)
        self.text_edit.setAlignment(Qt.AlignCenter)
        self.text_edit.setMaximumWidth(130)
        self.text_edit.setMaxLength(10)
        self.text_edit.textChanged.connect(self.check_exist)
        layout.addWidget(self.text_edit, 1, 0, 1, 1)
        # Create the label with a specified font size
        label = QLabel(self)
        label.setText(self.dict["save_button_label"])
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label, 2, 0, 2, 1)
        # Create button OK
        self.button = QPushButton(self.dict["save"])
        self.button.clicked.connect(lambda: self.parent.save_to_shelf(self.text_edit.text()))
        self.button.clicked.connect(self.close)
        layout.addWidget(self.button, 4, 0, 1, 1)
        layout.setAlignment(self.button, Qt.AlignCenter)

    def check_exist(self, shelf_name):
        if shelf_name in self.parent.shelf_workers():
            self.text_edit.setStyleSheet("color: %s;" % config.color_red())
            self.button.setText(self.dict["overwrite"])
        else:
            self.text_edit.setStyleSheet("")
            self.button.setText(self.dict["save"])


def run(dev=False, parent=None):
    dialog = SaveShelf(parent=parent)
    dialog.show()


if __name__ == '__main__':
    app = QApplication([])
    dialog = SaveShelf()
    dialog.exec_()
