# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_button.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(608, 148)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_button_bar = QHBoxLayout()
        self.layout_button_bar.setObjectName(u"layout_button_bar")
        self.button_add = QPushButton(Form)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setMaximumSize(QSize(20, 20))

        self.layout_button_bar.addWidget(self.button_add)

        self.button_close = QPushButton(Form)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setMaximumSize(QSize(20, 20))

        self.layout_button_bar.addWidget(self.button_close)

        self.button_name = QLineEdit(Form)
        self.button_name.setObjectName(u"button_name")
        self.button_name.setLayoutDirection(Qt.LeftToRight)
        self.button_name.setAlignment(Qt.AlignCenter)

        self.layout_button_bar.addWidget(self.button_name)

        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_button_bar.addItem(self.button_spacer)


        self.verticalLayout_2.addLayout(self.layout_button_bar)

        self.layout_button_script = QVBoxLayout()
        self.layout_button_script.setObjectName(u"layout_button_script")
        self.button_script = QPlainTextEdit(Form)
        self.button_script.setObjectName(u"button_script")

        self.layout_button_script.addWidget(self.button_script)


        self.verticalLayout_2.addLayout(self.layout_button_script)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.button_close.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.button_name.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u043a\u043d\u043e\u043f\u043a\u0438", None))
        self.button_script.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 python \u0441\u043a\u0440\u0438\u043f\u0442...", None))
    # retranslateUi

