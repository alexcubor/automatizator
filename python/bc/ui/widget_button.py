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
        Form.resize(837, 190)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_button_bar = QHBoxLayout()
        self.layout_button_bar.setObjectName(u"layout_button_bar")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.layout_button_bar.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_button_bar.addItem(self.horizontalSpacer)

        self.button_name = QLineEdit(Form)
        self.button_name.setObjectName(u"button_name")
        self.button_name.setLayoutDirection(Qt.LeftToRight)
        self.button_name.setAlignment(Qt.AlignCenter)

        self.layout_button_bar.addWidget(self.button_name)

        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_button_bar.addItem(self.button_spacer)

        self.button_open_script = QPushButton(Form)
        self.button_open_script.setObjectName(u"button_open_script")
        self.button_open_script.setMaximumSize(QSize(20, 20))

        self.layout_button_bar.addWidget(self.button_open_script)


        self.verticalLayout_2.addLayout(self.layout_button_bar)

        self.layout_button_script = QVBoxLayout()
        self.layout_button_script.setObjectName(u"layout_button_script")
        self.button_script = QPlainTextEdit(Form)
        self.button_script.setObjectName(u"button_script")
        self.button_script.setMaximumSize(QSize(16777215, 80))

        self.layout_button_script.addWidget(self.button_script)

        self.buttons_info = QLabel(Form)
        self.buttons_info.setObjectName(u"buttons_info")
        self.buttons_info.setLayoutDirection(Qt.LeftToRight)
        self.buttons_info.setTextFormat(Qt.PlainText)
        self.buttons_info.setAlignment(Qt.AlignCenter)
        self.buttons_info.setWordWrap(True)

        self.layout_button_script.addWidget(self.buttons_info)


        self.verticalLayout_2.addLayout(self.layout_button_script)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_name.setText(QCoreApplication.translate("Form", u"Button name", None))
        self.button_open_script.setText("")
        self.button_script.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 python \u0441\u043a\u0440\u0438\u043f\u0442, \u0447\u0442\u043e \u0431\u044b \u043a\u043d\u043e\u043f\u043a\u0430 \u043f\u043e\u044f\u0432\u0438\u043b\u0430\u0441\u044c \u0432 \u0447\u0435\u043a\u0435\u0440\u0435...", None))
        self.buttons_info.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u044f\u0441\u043d\u0435\u043d\u0438\u0435: \u043a\u043d\u043e\u043f\u043a\u0430 \u043f\u043e\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u0440\u0435\u0436\u0438\u043c\u0435 \u0447\u0435\u043a\u0435\u0440\u0430. \n"
"\u041e\u043d\u0430 \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0435\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438, \u0435\u0441\u043b\u0438 \u0432\u0441\u0435 \u044d\u0442\u0430\u043f\u044b \u043f\u0440\u043e\u0448\u043b\u0438 \u0443\u0441\u043f\u0435\u0448\u043d\u043e.", None))
    # retranslateUi

