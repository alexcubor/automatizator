# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'code_editor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CodeEditor(object):
    def setupUi(self, CodeEditor):
        if not CodeEditor.objectName():
            CodeEditor.setObjectName(u"CodeEditor")
        CodeEditor.resize(744, 445)
        self.verticalLayout_2 = QVBoxLayout(CodeEditor)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.edit_code = QPlainTextEdit(CodeEditor)
        self.edit_code.setObjectName(u"edit_code")

        self.main_layout.addWidget(self.edit_code)

        self.bottom_bar = QHBoxLayout()
        self.bottom_bar.setObjectName(u"bottom_bar")
        self.bottom_bar.setContentsMargins(-1, 0, -1, -1)
        self.call_line = QLabel(CodeEditor)
        self.call_line.setObjectName(u"call_line")

        self.bottom_bar.addWidget(self.call_line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottom_bar.addItem(self.horizontalSpacer)

        self.button_apply = QPushButton(CodeEditor)
        self.button_apply.setObjectName(u"button_apply")

        self.bottom_bar.addWidget(self.button_apply)

        self.button_accept = QPushButton(CodeEditor)
        self.button_accept.setObjectName(u"button_accept")

        self.bottom_bar.addWidget(self.button_accept)

        self.button_close = QPushButton(CodeEditor)
        self.button_close.setObjectName(u"button_close")

        self.bottom_bar.addWidget(self.button_close)


        self.main_layout.addLayout(self.bottom_bar)


        self.verticalLayout_2.addLayout(self.main_layout)


        self.retranslateUi(CodeEditor)

        QMetaObject.connectSlotsByName(CodeEditor)
    # setupUi

    def retranslateUi(self, CodeEditor):
        CodeEditor.setWindowTitle(QCoreApplication.translate("CodeEditor", u"Code Editor", None))
        self.call_line.setText(QCoreApplication.translate("CodeEditor", u"Ln 0 | Col 0", None))
        self.button_apply.setText(QCoreApplication.translate("CodeEditor", u"Apply", None))
        self.button_accept.setText(QCoreApplication.translate("CodeEditor", u"Accept", None))
        self.button_close.setText(QCoreApplication.translate("CodeEditor", u"Close", None))
    # retranslateUi

