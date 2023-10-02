# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worker_action.ui'
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
        Form.resize(400, 147)
        self.verticalLayout_2 = QVBoxLayout(Form)
#ifndef Q_OS_MAC
        self.verticalLayout_2.setSpacing(-1)
#endif
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, -1, -1, -1)
        self.progress_layout = QHBoxLayout()
#ifndef Q_OS_MAC
        self.progress_layout.setSpacing(-1)
#endif
        self.progress_layout.setObjectName(u"progress_layout")
        self.status = QLabel(Form)
        self.status.setObjectName(u"status")

        self.progress_layout.addWidget(self.status)

        self.status_spacer = QSpacerItem(4, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.progress_layout.addItem(self.status_spacer)

        self.action_name = QLabel(Form)
        self.action_name.setObjectName(u"action_name")

        self.progress_layout.addWidget(self.action_name)

        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.progress_layout.addItem(self.button_spacer)

        self.fix_button = QPushButton(Form)
        self.fix_button.setObjectName(u"fix_button")

        self.progress_layout.addWidget(self.fix_button)


        self.main_layout.addLayout(self.progress_layout)

        self.info = QPlainTextEdit(Form)
        self.info.setObjectName(u"info")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy)
        self.info.setFrameShape(QFrame.StyledPanel)
        self.info.setFrameShadow(QFrame.Sunken)
        self.info.setReadOnly(True)

        self.main_layout.addWidget(self.info)


        self.verticalLayout_2.addLayout(self.main_layout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.status.setText(QCoreApplication.translate("Form", u"Status", None))
        self.action_name.setText(QCoreApplication.translate("Form", u"Action name", None))
        self.fix_button.setText(QCoreApplication.translate("Form", u"Fix", None))
    # retranslateUi

