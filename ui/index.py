# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(922, 578)
        self.action_configs = QAction(MainWindow)
        self.action_configs.setObjectName(u"action_configs")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.comboBox)

        self.btn_sel_exchange = QPushButton(self.centralwidget)
        self.btn_sel_exchange.setObjectName(u"btn_sel_exchange")
        sizePolicy.setHeightForWidth(self.btn_sel_exchange.sizePolicy().hasHeightForWidth())
        self.btn_sel_exchange.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_sel_exchange)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.listWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbPluginName = QLabel(self.centralwidget)
        self.lbPluginName.setObjectName(u"lbPluginName")
        font = QFont()
        font.setPointSize(14)
        self.lbPluginName.setFont(font)
        self.lbPluginName.setScaledContents(False)

        self.verticalLayout_3.addWidget(self.lbPluginName)

        self.lbPluginInfo = QLabel(self.centralwidget)
        self.lbPluginInfo.setObjectName(u"lbPluginInfo")
        self.lbPluginInfo.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lbPluginInfo)

        self.layout_main = QVBoxLayout()
        self.layout_main.setObjectName(u"layout_main")

        self.verticalLayout_3.addLayout(self.layout_main)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.btn_helper = QPushButton(self.centralwidget)
        self.btn_helper.setObjectName(u"btn_helper")
        sizePolicy.setHeightForWidth(self.btn_helper.sizePolicy().hasHeightForWidth())
        self.btn_helper.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btn_helper)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        sizePolicy.setHeightForWidth(self.btn_copy.sizePolicy().hasHeightForWidth())
        self.btn_copy.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btn_copy)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.textBrowser)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CCTX-Helper", None))
        self.action_configs.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u914d\u7f6e", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u4ee3\u7406", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u6240", None))
        self.btn_sel_exchange.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u5217\u8868", None))
        self.lbPluginName.setText("")
        self.lbPluginInfo.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u6e90\u6216\u64cd\u4f5c\u63d0\u793a", None))
        self.btn_helper.setText(QCoreApplication.translate("MainWindow", u"\u6587\u6863", None))
        self.btn_copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
    # retranslateUi

