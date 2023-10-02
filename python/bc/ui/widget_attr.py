# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_attr.ui'
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
        Form.resize(648, 61)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout_attr = QHBoxLayout()
        self.layout_attr.setObjectName(u"layout_attr")
        self.layout_attr.setContentsMargins(-1, -1, -1, 0)
        self.attr_button_add = QPushButton(Form)
        self.attr_button_add.setObjectName(u"attr_button_add")
        self.attr_button_add.setMinimumSize(QSize(20, 20))
        self.attr_button_add.setMaximumSize(QSize(20, 20))

        self.layout_attr.addWidget(self.attr_button_add)

        self.attr_close = QPushButton(Form)
        self.attr_close.setObjectName(u"attr_close")
        self.attr_close.setMinimumSize(QSize(20, 20))
        self.attr_close.setMaximumSize(QSize(20, 20))

        self.layout_attr.addWidget(self.attr_close)

        self.attr_type = QLineEdit(Form)
        self.attr_type.setObjectName(u"attr_type")
        self.attr_type.setMinimumSize(QSize(0, 25))

        self.layout_attr.addWidget(self.attr_type)

        self.attr_name = QLineEdit(Form)
        self.attr_name.setObjectName(u"attr_name")
        self.attr_name.setMinimumSize(QSize(220, 25))

        self.layout_attr.addWidget(self.attr_name)

        self.attr_label_to = QLabel(Form)
        self.attr_label_to.setObjectName(u"attr_label_to")

        self.layout_attr.addWidget(self.attr_label_to)

        self.attr_value = QLineEdit(Form)
        self.attr_value.setObjectName(u"attr_value")
        self.attr_value.setMinimumSize(QSize(0, 25))
        self.attr_value.setMaximumSize(QSize(16777215, 16777215))

        self.layout_attr.addWidget(self.attr_value)


        self.horizontalLayout.addLayout(self.layout_attr)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"attr", None))
        self.attr_button_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.attr_close.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.attr_type.setPlaceholderText(QCoreApplication.translate("Form", u"typeNode", None))
        self.attr_name.setPlaceholderText(QCoreApplication.translate("Form", u"nodeName.attrName", None))
        self.attr_label_to.setText(QCoreApplication.translate("Form", u"=", None))
        self.attr_value.setPlaceholderText(QCoreApplication.translate("Form", u"value", None))
    # retranslateUi

