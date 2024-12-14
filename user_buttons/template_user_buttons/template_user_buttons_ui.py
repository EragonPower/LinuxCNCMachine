# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/buildbot/buildbot/worker/probe_basic-dev/sources/debian/python3-probe-basic/usr/share/configs/machine_setup_files/user_buttons/template_user_buttons/template_user_buttons.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_USER_BUTTONS(object):
    def setupUi(self, USER_BUTTONS):
        USER_BUTTONS.setObjectName("USER_BUTTONS")
        USER_BUTTONS.resize(285, 196)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(USER_BUTTONS.sizePolicy().hasHeightForWidth())
        USER_BUTTONS.setSizePolicy(sizePolicy)
        USER_BUTTONS.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout = QtWidgets.QGridLayout(USER_BUTTONS)
        self.gridLayout.setContentsMargins(1, 3, 1, 1)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.block_delete_button = ActionButton(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.block_delete_button.sizePolicy().hasHeightForWidth())
        self.block_delete_button.setSizePolicy(sizePolicy)
        self.block_delete_button.setMinimumSize(QtCore.QSize(135, 42))
        self.block_delete_button.setMaximumSize(QtCore.QSize(16777215, 42))
        self.block_delete_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.block_delete_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.block_delete_button.setCheckable(True)
        self.block_delete_button.setObjectName("block_delete_button")
        self.gridLayout.addWidget(self.block_delete_button, 2, 2, 1, 1)
        self.m01_break_button = ActionButton(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m01_break_button.sizePolicy().hasHeightForWidth())
        self.m01_break_button.setSizePolicy(sizePolicy)
        self.m01_break_button.setMinimumSize(QtCore.QSize(135, 42))
        self.m01_break_button.setMaximumSize(QtCore.QSize(16777215, 42))
        self.m01_break_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m01_break_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.m01_break_button.setCheckable(True)
        self.m01_break_button.setObjectName("m01_break_button")
        self.gridLayout.addWidget(self.m01_break_button, 3, 2, 1, 1)
        self.flood_button = ActionButton(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flood_button.sizePolicy().hasHeightForWidth())
        self.flood_button.setSizePolicy(sizePolicy)
        self.flood_button.setMinimumSize(QtCore.QSize(135, 42))
        self.flood_button.setMaximumSize(QtCore.QSize(16777215, 42))
        self.flood_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.flood_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.flood_button.setCheckable(True)
        self.flood_button.setObjectName("flood_button")
        self.gridLayout.addWidget(self.flood_button, 2, 0, 1, 1)
        self.single_block_button = ActionButton(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.single_block_button.sizePolicy().hasHeightForWidth())
        self.single_block_button.setSizePolicy(sizePolicy)
        self.single_block_button.setMinimumSize(QtCore.QSize(135, 42))
        self.single_block_button.setMaximumSize(QtCore.QSize(16777215, 42))
        self.single_block_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.single_block_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.single_block_button.setObjectName("single_block_button")
        self.gridLayout.addWidget(self.single_block_button, 1, 2, 1, 1)
        self.mist_button = ActionButton(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mist_button.sizePolicy().hasHeightForWidth())
        self.mist_button.setSizePolicy(sizePolicy)
        self.mist_button.setMinimumSize(QtCore.QSize(135, 42))
        self.mist_button.setMaximumSize(QtCore.QSize(16777215, 42))
        self.mist_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mist_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.mist_button.setCheckable(True)
        self.mist_button.setObjectName("mist_button")
        self.gridLayout.addWidget(self.mist_button, 3, 0, 1, 1)
        self.feed_hold_button = ActionButton(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feed_hold_button.sizePolicy().hasHeightForWidth())
        self.feed_hold_button.setSizePolicy(sizePolicy)
        self.feed_hold_button.setMinimumSize(QtCore.QSize(135, 42))
        self.feed_hold_button.setMaximumSize(QtCore.QSize(16777215, 42))
        self.feed_hold_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.feed_hold_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.feed_hold_button.setCheckable(True)
        self.feed_hold_button.setObjectName("feed_hold_button")
        self.gridLayout.addWidget(self.feed_hold_button, 0, 2, 1, 1)
        self.clear_program_button = ActionButton(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_program_button.sizePolicy().hasHeightForWidth())
        self.clear_program_button.setSizePolicy(sizePolicy)
        self.clear_program_button.setMinimumSize(QtCore.QSize(135, 42))
        self.clear_program_button.setMaximumSize(QtCore.QSize(16777215, 42))
        self.clear_program_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_program_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.clear_program_button.setCheckable(False)
        self.clear_program_button.setObjectName("clear_program_button")
        self.gridLayout.addWidget(self.clear_program_button, 1, 0, 1, 1)
        self.reload_program_button = ActionButton(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reload_program_button.sizePolicy().hasHeightForWidth())
        self.reload_program_button.setSizePolicy(sizePolicy)
        self.reload_program_button.setMinimumSize(QtCore.QSize(135, 42))
        self.reload_program_button.setMaximumSize(QtCore.QSize(16777215, 42))
        self.reload_program_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.reload_program_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reload_program_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.reload_program_button.setCheckable(False)
        self.reload_program_button.setObjectName("reload_program_button")
        self.gridLayout.addWidget(self.reload_program_button, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(USER_BUTTONS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        self.retranslateUi(USER_BUTTONS)
        QtCore.QMetaObject.connectSlotsByName(USER_BUTTONS)

    def retranslateUi(self, USER_BUTTONS):
        _translate = QtCore.QCoreApplication.translate
        USER_BUTTONS.setWindowTitle(_translate("USER_BUTTONS", "User Buttons"))
        self.block_delete_button.setText(_translate("USER_BUTTONS", "BLOCK DELETE"))
        self.block_delete_button.setProperty("actionName", _translate("USER_BUTTONS", "program.block-delete.toggle"))
        self.m01_break_button.setText(_translate("USER_BUTTONS", "M01 BREAK"))
        self.m01_break_button.setProperty("actionName", _translate("USER_BUTTONS", "program.optional-stop.toggle"))
        self.flood_button.setText(_translate("USER_BUTTONS", "Flood"))
        self.flood_button.setProperty("actionName", _translate("USER_BUTTONS", "coolant.flood.toggle"))
        self.single_block_button.setText(_translate("USER_BUTTONS", "SINGLE BLOCK"))
        self.single_block_button.setProperty("actionName", _translate("USER_BUTTONS", "program.step"))
        self.mist_button.setText(_translate("USER_BUTTONS", "Mist"))
        self.mist_button.setProperty("actionName", _translate("USER_BUTTONS", "coolant.mist.toggle"))
        self.feed_hold_button.setText(_translate("USER_BUTTONS", "FEED HOLD"))
        self.feed_hold_button.setProperty("rules", _translate("USER_BUTTONS", "[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == \'Paused\'\", \"name\": \"check when paused\"}]"))
        self.feed_hold_button.setProperty("actionName", _translate("USER_BUTTONS", "program.pause"))
        self.clear_program_button.setText(_translate("USER_BUTTONS", "CLEAR PGM"))
        self.clear_program_button.setProperty("actionName", _translate("USER_BUTTONS", "program.clear"))
        self.reload_program_button.setText(_translate("USER_BUTTONS", "RELOAD PGM"))
        self.reload_program_button.setProperty("actionName", _translate("USER_BUTTONS", "program.reload"))
from qtpyvcp.widgets.button_widgets.action_button import ActionButton
