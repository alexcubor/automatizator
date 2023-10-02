# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_action.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_widget_action(object):
    def setupUi(self, widget_action):
        if not widget_action.objectName():
            widget_action.setObjectName(u"widget_action")
        widget_action.resize(764, 671)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_action.sizePolicy().hasHeightForWidth())
        widget_action.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(widget_action)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_action = QHBoxLayout()
        self.layout_action.setObjectName(u"layout_action")
        self.layout_action.setContentsMargins(-1, 0, -1, -1)
        self.layout_bar = QVBoxLayout()
        self.layout_bar.setObjectName(u"layout_bar")
        self.layout_bar.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_bar.setContentsMargins(0, -1, 0, 0)
        self.spacer_close_top = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.layout_bar.addItem(self.spacer_close_top)

        self.button_collapse = QPushButton(widget_action)
        self.button_collapse.setObjectName(u"button_collapse")
        self.button_collapse.setMaximumSize(QSize(20, 20))

        self.layout_bar.addWidget(self.button_collapse)

        self.button_mute = QPushButton(widget_action)
        self.button_mute.setObjectName(u"button_mute")
        self.button_mute.setMinimumSize(QSize(20, 20))
        self.button_mute.setMaximumSize(QSize(20, 20))
        self.button_mute.setStyleSheet(u"button.setStyleSheet(\"QPushButton:hover { background-color: lightcoral; }\")")

        self.layout_bar.addWidget(self.button_mute)

        self.button_close = QPushButton(widget_action)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setMinimumSize(QSize(20, 20))
        self.button_close.setMaximumSize(QSize(20, 20))

        self.layout_bar.addWidget(self.button_close)

        self.spacer_button = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_bar.addItem(self.spacer_button)


        self.layout_action.addLayout(self.layout_bar)

        self.layout_mode = QVBoxLayout()
        self.layout_mode.setObjectName(u"layout_mode")
        self.layout_title = QHBoxLayout()
        self.layout_title.setObjectName(u"layout_title")
        self.title_action = QTextEdit(widget_action)
        self.title_action.setObjectName(u"title_action")
        self.title_action.setMinimumSize(QSize(0, 31))
        self.title_action.setMaximumSize(QSize(16777215, 28))
        font = QFont()
        font.setPointSize(16)
        self.title_action.setFont(font)
        self.title_action.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.layout_title.addWidget(self.title_action)


        self.layout_mode.addLayout(self.layout_title)

        self.frame_action = QFrame(widget_action)
        self.frame_action.setObjectName(u"frame_action")
        sizePolicy.setHeightForWidth(self.frame_action.sizePolicy().hasHeightForWidth())
        self.frame_action.setSizePolicy(sizePolicy)
        self.frame_action.setMinimumSize(QSize(0, 0))
        self.frame_action.setFrameShape(QFrame.Box)
        self.frame_action.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame_action)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.layout_rule = QHBoxLayout()
#ifndef Q_OS_MAC
        self.layout_rule.setSpacing(-1)
#endif
        self.layout_rule.setObjectName(u"layout_rule")
        self.layout_rule.setContentsMargins(-1, 0, 0, 0)
        self.run_label = QLabel(self.frame_action)
        self.run_label.setObjectName(u"run_label")

        self.layout_rule.addWidget(self.run_label)

        self.run_menu = QToolButton(self.frame_action)
        self.run_menu.setObjectName(u"run_menu")

        self.layout_rule.addWidget(self.run_menu)

        self.run_pattern = QLineEdit(self.frame_action)
        self.run_pattern.setObjectName(u"run_pattern")
        self.run_pattern.setMinimumSize(QSize(0, 25))

        self.layout_rule.addWidget(self.run_pattern)

        self.override_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_rule.addItem(self.override_spacer)


        self.verticalLayout_2.addLayout(self.layout_rule)

        self.tool_run = QHBoxLayout()
        self.tool_run.setObjectName(u"tool_run")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tool_run.addItem(self.horizontalSpacer)

        self.button_open_script_run = QPushButton(self.frame_action)
        self.button_open_script_run.setObjectName(u"button_open_script_run")
        self.button_open_script_run.setMaximumSize(QSize(20, 20))

        self.tool_run.addWidget(self.button_open_script_run)


        self.verticalLayout_2.addLayout(self.tool_run)

        self.layout_script_run = QVBoxLayout()
        self.layout_script_run.setObjectName(u"layout_script_run")
        self.layout_script_run.setContentsMargins(-1, 0, -1, -1)
        self.action_script_run = QTextEdit(self.frame_action)
        self.action_script_run.setObjectName(u"action_script_run")
        sizePolicy.setHeightForWidth(self.action_script_run.sizePolicy().hasHeightForWidth())
        self.action_script_run.setSizePolicy(sizePolicy)
        self.action_script_run.setMinimumSize(QSize(0, 80))
        self.action_script_run.setMaximumSize(QSize(16777215, 80))

        self.layout_script_run.addWidget(self.action_script_run)


        self.verticalLayout_2.addLayout(self.layout_script_run)

        self.layout_select_mode = QHBoxLayout()
        self.layout_select_mode.setObjectName(u"layout_select_mode")
        self.type_label = QLabel(self.frame_action)
        self.type_label.setObjectName(u"type_label")

        self.layout_select_mode.addWidget(self.type_label)

        self.type_menu = QToolButton(self.frame_action)
        self.type_menu.setObjectName(u"type_menu")

        self.layout_select_mode.addWidget(self.type_menu)

        self.spacer_select_mode = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_select_mode.addItem(self.spacer_select_mode)


        self.verticalLayout_2.addLayout(self.layout_select_mode)

        self.tool_builder = QHBoxLayout()
        self.tool_builder.setObjectName(u"tool_builder")
        self.tool_builder.setContentsMargins(-1, 0, -1, -1)
        self.enable_builder = QCheckBox(self.frame_action)
        self.enable_builder.setObjectName(u"enable_builder")
        self.enable_builder.setEnabled(True)
        self.enable_builder.setTabletTracking(False)
        self.enable_builder.setAcceptDrops(False)
        self.enable_builder.setChecked(True)

        self.tool_builder.addWidget(self.enable_builder)

        self.button_open_script_builder = QPushButton(self.frame_action)
        self.button_open_script_builder.setObjectName(u"button_open_script_builder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_open_script_builder.sizePolicy().hasHeightForWidth())
        self.button_open_script_builder.setSizePolicy(sizePolicy1)
        self.button_open_script_builder.setMaximumSize(QSize(20, 20))

        self.tool_builder.addWidget(self.button_open_script_builder)


        self.verticalLayout_2.addLayout(self.tool_builder)

        self.widget_attrs = QWidget(self.frame_action)
        self.widget_attrs.setObjectName(u"widget_attrs")
        self.widget_attrs.setMinimumSize(QSize(0, 0))
        self.layout_attr = QVBoxLayout(self.widget_attrs)
        self.layout_attr.setObjectName(u"layout_attr")
        self.layout_attr.setContentsMargins(-1, 1, -1, -1)
        self.layout_attrs = QVBoxLayout()
        self.layout_attrs.setObjectName(u"layout_attrs")

        self.layout_attr.addLayout(self.layout_attrs)


        self.verticalLayout_2.addWidget(self.widget_attrs)

        self.layout_script_build = QVBoxLayout()
        self.layout_script_build.setObjectName(u"layout_script_build")
        self.layout_script_build.setContentsMargins(-1, 0, -1, -1)
        self.action_script_build = QPlainTextEdit(self.frame_action)
        self.action_script_build.setObjectName(u"action_script_build")
        sizePolicy.setHeightForWidth(self.action_script_build.sizePolicy().hasHeightForWidth())
        self.action_script_build.setSizePolicy(sizePolicy)
        self.action_script_build.setMinimumSize(QSize(0, 80))
        self.action_script_build.setMaximumSize(QSize(16777215, 80))

        self.layout_script_build.addWidget(self.action_script_build)


        self.verticalLayout_2.addLayout(self.layout_script_build)

        self.tool_checker = QHBoxLayout()
        self.tool_checker.setObjectName(u"tool_checker")
        self.tool_checker.setContentsMargins(-1, 0, -1, -1)
        self.enable_checker = QCheckBox(self.frame_action)
        self.enable_checker.setObjectName(u"enable_checker")
        self.enable_checker.setChecked(True)

        self.tool_checker.addWidget(self.enable_checker)

        self.button_open_script_checker = QPushButton(self.frame_action)
        self.button_open_script_checker.setObjectName(u"button_open_script_checker")
        self.button_open_script_checker.setMaximumSize(QSize(20, 20))

        self.tool_checker.addWidget(self.button_open_script_checker)


        self.verticalLayout_2.addLayout(self.tool_checker)

        self.action_script_check = QPlainTextEdit(self.frame_action)
        self.action_script_check.setObjectName(u"action_script_check")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.action_script_check.sizePolicy().hasHeightForWidth())
        self.action_script_check.setSizePolicy(sizePolicy2)
        self.action_script_check.setMinimumSize(QSize(0, 80))
        self.action_script_check.setMaximumSize(QSize(16777215, 80))
        self.action_script_check.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_2.addWidget(self.action_script_check)

        self.layout_override = QHBoxLayout()
        self.layout_override.setObjectName(u"layout_override")
        self.spacer_override = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_override.addItem(self.spacer_override)

        self.menu_override = QToolButton(self.frame_action)
        self.menu_override.setObjectName(u"menu_override")

        self.layout_override.addWidget(self.menu_override)

        self.button_add_override_action = QPushButton(self.frame_action)
        self.button_add_override_action.setObjectName(u"button_add_override_action")
        self.button_add_override_action.setMinimumSize(QSize(20, 20))
        self.button_add_override_action.setMaximumSize(QSize(120, 20))

        self.layout_override.addWidget(self.button_add_override_action)


        self.verticalLayout_2.addLayout(self.layout_override)

        self.layout_override_action = QVBoxLayout()
        self.layout_override_action.setObjectName(u"layout_override_action")

        self.verticalLayout_2.addLayout(self.layout_override_action)


        self.layout_mode.addWidget(self.frame_action)


        self.layout_action.addLayout(self.layout_mode)


        self.verticalLayout.addLayout(self.layout_action)

        self.spacer_before_add = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.spacer_before_add)

        self.layout_add_action = QHBoxLayout()
        self.layout_add_action.setObjectName(u"layout_add_action")
        self.layout_add_action.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_add_action.setContentsMargins(-1, 0, -1, -1)
        self.button_add_action = QPushButton(widget_action)
        self.button_add_action.setObjectName(u"button_add_action")
        self.button_add_action.setMaximumSize(QSize(100, 18))

        self.layout_add_action.addWidget(self.button_add_action)


        self.verticalLayout.addLayout(self.layout_add_action)


        self.retranslateUi(widget_action)

        QMetaObject.connectSlotsByName(widget_action)
    # setupUi

    def retranslateUi(self, widget_action):
        widget_action.setWindowTitle(QCoreApplication.translate("widget_action", u"Form", None))
        self.button_collapse.setText(QCoreApplication.translate("widget_action", u"v", None))
        self.button_mute.setText(QCoreApplication.translate("widget_action", u"M", None))
        self.button_close.setText(QCoreApplication.translate("widget_action", u"\u00d7", None))
        self.title_action.setPlaceholderText(QCoreApplication.translate("widget_action", u"Name the action", None))
        self.run_label.setText(QCoreApplication.translate("widget_action", u"Run", None))
        self.run_menu.setText(QCoreApplication.translate("widget_action", u"Every time   ", None))
        self.run_pattern.setPlaceholderText(QCoreApplication.translate("widget_action", u"pattern*.ext", None))
        self.button_open_script_run.setText("")
        self.action_script_run.setPlaceholderText(QCoreApplication.translate("widget_action", u"Write python script...", None))
        self.type_label.setText(QCoreApplication.translate("widget_action", u"Type", None))
        self.type_menu.setText(QCoreApplication.translate("widget_action", u"Select action type...   ", None))
        self.enable_builder.setText(QCoreApplication.translate("widget_action", u"Enable builder", None))
        self.button_open_script_builder.setText("")
        self.action_script_build.setPlaceholderText(QCoreApplication.translate("widget_action", u"Write python script...", None))
        self.enable_checker.setText(QCoreApplication.translate("widget_action", u"Enable checker", None))
        self.button_open_script_checker.setText("")
        self.action_script_check.setPlaceholderText(QCoreApplication.translate("widget_action", u"Write python script...", None))
        self.menu_override.setText(QCoreApplication.translate("widget_action", u"Run instead parent action", None))
        self.button_add_override_action.setText(QCoreApplication.translate("widget_action", u"Add override +", None))
        self.button_add_action.setText(QCoreApplication.translate("widget_action", u"+", None))
    # retranslateUi

