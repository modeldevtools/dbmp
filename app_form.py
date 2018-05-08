# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from custom_tableview import CustomTableView

class Ui_qdTest(object):
    def setupUi(self, qdTest):
        qdTest.setObjectName("qdTest")
        qdTest.resize(635, 560)
        self.verticalLayout = QtWidgets.QVBoxLayout(qdTest)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hblConnection = QtWidgets.QHBoxLayout()
        self.hblConnection.setObjectName("hblConnection")
        self.gpbConnection = QtWidgets.QGroupBox(qdTest)
        self.gpbConnection.setObjectName("gpbConnection")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.gpbConnection)
        self.horizontalLayout_3.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmbProvider = QtWidgets.QComboBox(self.gpbConnection)
        self.cmbProvider.setObjectName("cmbProvider")
        self.horizontalLayout_3.addWidget(self.cmbProvider)
        self.leConnection = QtWidgets.QLineEdit(self.gpbConnection)
        self.leConnection.setObjectName("leConnection")
        self.horizontalLayout_3.addWidget(self.leConnection)
        self.pbCheck = QtWidgets.QPushButton(self.gpbConnection)
        self.pbCheck.setObjectName("pbCheck")
        self.horizontalLayout_3.addWidget(self.pbCheck)
        self.hblConnection.addWidget(self.gpbConnection)
        self.line = QtWidgets.QFrame(qdTest)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hblConnection.addWidget(self.line)
        self.groupBox = QtWidgets.QGroupBox(qdTest)
        self.groupBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.leRowsPerPage = QtWidgets.QLineEdit(self.groupBox)
        self.leRowsPerPage.setMaximumSize(QtCore.QSize(70, 16777215))
        self.leRowsPerPage.setText("")
        self.leRowsPerPage.setObjectName("leRowsPerPage")
        self.horizontalLayout_5.addWidget(self.leRowsPerPage)
        self.hblConnection.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.hblConnection)
        self.hblQuery = QtWidgets.QHBoxLayout()
        self.hblQuery.setObjectName("hblQuery")
        self.gpbQuery = QtWidgets.QGroupBox(qdTest)
        self.gpbQuery.setObjectName("gpbQuery")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.gpbQuery)
        self.horizontalLayout_4.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.teQuery = QtWidgets.QTextEdit(self.gpbQuery)
        self.teQuery.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teQuery.sizePolicy().hasHeightForWidth())
        self.teQuery.setSizePolicy(sizePolicy)
        self.teQuery.setMinimumSize(QtCore.QSize(0, 100))
        self.teQuery.setMaximumSize(QtCore.QSize(16777215, 192))
        self.teQuery.setObjectName("teQuery")
        self.horizontalLayout_4.addWidget(self.teQuery)
        self.pbExecute = QtWidgets.QPushButton(self.gpbQuery)
        self.pbExecute.setObjectName("pbExecute")
        self.horizontalLayout_4.addWidget(self.pbExecute)
        self.hblQuery.addWidget(self.gpbQuery)
        self.verticalLayout.addLayout(self.hblQuery)
        self.hblResults = QtWidgets.QHBoxLayout()
        self.hblResults.setObjectName("hblResults")
        self.gpbResults = QtWidgets.QGroupBox(qdTest)
        self.gpbResults.setObjectName("gpbResults")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gpbResults)
        self.verticalLayout_2.setContentsMargins(7, 7, 7, 7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.tbvResults = QtWidgets.QTableView(self.gpbResults)
        self.tbvResults = CustomTableView(self.gpbResults)
        self.tbvResults.setFrameShape(QtWidgets.QFrame.Panel)
        self.tbvResults.setObjectName("tbvResults")
        self.tbvResults.horizontalHeader().setVisible(True)
        self.verticalLayout_2.addWidget(self.tbvResults)
        self.hblForthBack = QtWidgets.QHBoxLayout()
        self.hblForthBack.setObjectName("hblForthBack")
        self.pbBack = QtWidgets.QPushButton(self.gpbResults)
        self.pbBack.setObjectName("pbBack")
        self.hblForthBack.addWidget(self.pbBack)
        self.lblPage = QtWidgets.QLabel(self.gpbResults)
        self.lblPage.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lblPage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPage.setObjectName("lblPage")
        self.hblForthBack.addWidget(self.lblPage)
        self.frmPage = QtWidgets.QFrame(self.gpbResults)
        self.frmPage.setMaximumSize(QtCore.QSize(100, 28))
        self.frmPage.setFrameShape(QtWidgets.QFrame.Panel)
        self.frmPage.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmPage.setObjectName("frmPage")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frmPage)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblCurrentPage = QtWidgets.QLabel(self.frmPage)
        self.lblCurrentPage.setText("")
        self.lblCurrentPage.setObjectName("lblCurrentPage")
        self.horizontalLayout.addWidget(self.lblCurrentPage)
        self.hblForthBack.addWidget(self.frmPage)
        self.pbForth = QtWidgets.QPushButton(self.gpbResults)
        self.pbForth.setObjectName("pbForth")
        self.hblForthBack.addWidget(self.pbForth)
        self.verticalLayout_2.addLayout(self.hblForthBack)
        self.hblResults.addWidget(self.gpbResults)
        self.verticalLayout.addLayout(self.hblResults)
        self.hblClose = QtWidgets.QHBoxLayout()
        self.hblClose.setObjectName("hblClose")
        self.lblUpdate = QtWidgets.QLabel(qdTest)
        self.lblUpdate.setObjectName("lblUpdate")
        self.hblClose.addWidget(self.lblUpdate)
        self.frmUpdate = QtWidgets.QFrame(qdTest)
        self.frmUpdate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmUpdate.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmUpdate.setObjectName("frmUpdate")
        self.hblClose.addWidget(self.frmUpdate)
        self.lblUpdateTime = QtWidgets.QLabel(qdTest)
        self.lblUpdateTime.setMinimumSize(QtCore.QSize(100, 0))
        self.lblUpdateTime.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblUpdateTime.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblUpdateTime.setText("")
        self.lblUpdateTime.setObjectName("lblUpdateTime")
        self.hblClose.addWidget(self.lblUpdateTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hblClose.addItem(spacerItem)
        self.pbClose = QtWidgets.QPushButton(qdTest)
        self.pbClose.setObjectName("pbClose")
        self.hblClose.addWidget(self.pbClose)
        self.verticalLayout.addLayout(self.hblClose)

        self.retranslateUi(qdTest)
        QtCore.QMetaObject.connectSlotsByName(qdTest)

    def retranslateUi(self, qdTest):
        _translate = QtCore.QCoreApplication.translate
        qdTest.setWindowTitle(_translate("qdTest", "Test Application"))
        self.gpbConnection.setTitle(_translate("qdTest", "Connection string"))
        self.leConnection.setText(_translate("qdTest", ":memory:"))
        self.pbCheck.setText(_translate("qdTest", "Check"))
        self.groupBox.setTitle(_translate("qdTest", "Rows per page"))
        self.leRowsPerPage.setInputMask(_translate("qdTest", "999999;0"))
        self.gpbQuery.setTitle(_translate("qdTest", "Query string"))
        self.pbExecute.setToolTip(_translate("qdTest", "Ctrl+Enter"))
        self.pbExecute.setText(_translate("qdTest", "Execute"))
        self.gpbResults.setTitle(_translate("qdTest", "Results"))
        self.pbBack.setText(_translate("qdTest", "< Back"))
        self.lblPage.setText(_translate("qdTest", "Current page:"))
        self.pbForth.setText(_translate("qdTest", "Forth >"))
        self.lblUpdate.setText(_translate("qdTest", "Results updated:"))
        self.pbClose.setText(_translate("qdTest", "Close"))
