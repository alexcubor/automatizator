# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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
        Dialog.resize(608, 299)
        Dialog.setMinimumSize(QSize(453, 0))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_bar = QHBoxLayout()
        self.layout_bar.setObjectName(u"layout_bar")
        self.menu_file = QToolButton(Dialog)
        self.menu_file.setObjectName(u"menu_file")

        self.layout_bar.addWidget(self.menu_file)

        self.menu_settings = QToolButton(Dialog)
        self.menu_settings.setObjectName(u"menu_settings")

        self.layout_bar.addWidget(self.menu_settings)

        self.menu_help = QToolButton(Dialog)
        self.menu_help.setObjectName(u"menu_help")

        self.layout_bar.addWidget(self.menu_help)

        self.spacer_menu = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_bar.addItem(self.spacer_menu)


        self.verticalLayout_2.addLayout(self.layout_bar)

        self.scroll_main = QScrollArea(Dialog)
        self.scroll_main.setObjectName(u"scroll_main")
        self.scroll_main.setFrameShape(QFrame.NoFrame)
        self.scroll_main.setWidgetResizable(True)
        self.widget_main = QWidget()
        self.widget_main.setObjectName(u"widget_main")
        self.widget_main.setGeometry(QRect(0, 0, 584, 241))
        self.verticalLayout = QVBoxLayout(self.widget_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_add_action = QHBoxLayout()
        self.layout_add_action.setObjectName(u"layout_add_action")
        self.layout_add_action.setContentsMargins(-1, 0, -1, -1)
        self.button_add_action0 = QPushButton(self.widget_main)
        self.button_add_action0.setObjectName(u"button_add_action0")
        self.button_add_action0.setMaximumSize(QSize(100, 18))

        self.layout_add_action.addWidget(self.button_add_action0)


        self.verticalLayout.addLayout(self.layout_add_action)

        self.layout_tabs = QVBoxLayout()
        self.layout_tabs.setObjectName(u"layout_tabs")
        self.layout_tabs.setContentsMargins(-1, 0, -1, -1)

        self.verticalLayout.addLayout(self.layout_tabs)

        self.buttons_info = QLabel(self.widget_main)
        self.buttons_info.setObjectName(u"buttons_info")
        self.buttons_info.setTextFormat(Qt.AutoText)
        self.buttons_info.setScaledContents(False)
        self.buttons_info.setWordWrap(True)

        self.verticalLayout.addWidget(self.buttons_info)

        self.layout_buttons = QVBoxLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")

        self.verticalLayout.addLayout(self.layout_buttons)

        self.spacer_dialog = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.spacer_dialog)

        self.scroll_main.setWidget(self.widget_main)

        self.verticalLayout_2.addWidget(self.scroll_main)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Automatizator", None))
        self.menu_file.setText(QCoreApplication.translate("Dialog", u"File", None))
        self.menu_settings.setText(QCoreApplication.translate("Dialog", u"Settings", None))
        self.menu_help.setText(QCoreApplication.translate("Dialog", u"Help", None))
        self.button_add_action0.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.buttons_info.setText(QCoreApplication.translate("Dialog", u"\u041a\u043d\u043e\u043f\u043a\u0438 \u043f\u043e\u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u0440\u0435\u0436\u0438\u043c\u0435 \u0447\u0435\u043a\u0435\u0440\u0430 \u0438 \u0441\u0442\u0430\u043d\u043e\u0432\u044f\u0442\u0441\u044f \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u043c\u0438 \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u043e\u0441\u043b\u0435 \u0435\u0433\u043e \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f.", None))
    # retranslateUi

