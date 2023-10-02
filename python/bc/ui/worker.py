# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worker.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 600)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scroll_area = QScrollArea(Dialog)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.scroll_widget.setGeometry(QRect(0, 0, 374, 550))
        self.scroll_widget.setMaximumSize(QSize(374, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.scroll_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setObjectName(u"scroll_layout")

        self.verticalLayout_3.addLayout(self.scroll_layout)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scroll_area.setWidget(self.scroll_widget)

        self.verticalLayout.addWidget(self.scroll_area)

        self.progress_bar = QProgressBar(Dialog)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(24)

        self.verticalLayout.addWidget(self.progress_bar)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

