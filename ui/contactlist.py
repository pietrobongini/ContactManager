# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactlist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mw = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 508)
        MainWindow.setMinimumSize(QtCore.QSize(301, 508))
        MainWindow.setMaximumSize(QtCore.QSize(301, 508))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 105, 301, 361))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setKerning(True)
        self.scrollArea.setFont(font)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 301, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonListLayout = QtWidgets.QVBoxLayout()
        self.buttonListLayout.setContentsMargins(-1, -1, -1, 0)
        self.buttonListLayout.setObjectName("buttonListLayout")
        self.verticalLayout_2.addLayout(self.buttonListLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(215, 70, 81, 31))
        self.search_button.setObjectName("search_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 5, 135, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(250, 3, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.add_button.setFont(font)
        self.add_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/add_symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.add_button.setIcon(icon)
        self.add_button.setAutoRepeatDelay(300)
        self.add_button.setObjectName("add_button")
        self.tag_button = QtWidgets.QPushButton(self.centralwidget)
        self.tag_button.setGeometry(QtCore.QRect(4, 0, 61, 41))
        self.tag_button.setObjectName("tag_button")
        self.search_text = QtWidgets.QLineEdit(self.centralwidget)
        self.search_text.setGeometry(QtCore.QRect(12, 45, 196, 21))
        self.search_text.setObjectName("search_text")
        self.tagBox = QtWidgets.QComboBox(self.centralwidget)
        self.tagBox.setGeometry(QtCore.QRect(10, 70, 201, 26))
        self.tagBox.setObjectName("tagBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 301, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "CONTACTS"))
        self.tag_button.setText(_translate("MainWindow", "Tag"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

