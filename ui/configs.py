# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configs.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTextBrowser, QWidget)

class Ui_configs(object):
    def setupUi(self, configs):
        if not configs.objectName():
            configs.setObjectName(u"configs")
        configs.resize(843, 549)
        self.groupBox = QGroupBox(configs)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 281, 211))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 53, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 53, 16))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 130, 53, 16))
        self.txt_api_key = QLineEdit(self.groupBox)
        self.txt_api_key.setObjectName(u"txt_api_key")
        self.txt_api_key.setGeometry(QRect(10, 40, 261, 21))
        self.txt_secret = QLineEdit(self.groupBox)
        self.txt_secret.setObjectName(u"txt_secret")
        self.txt_secret.setGeometry(QRect(10, 100, 261, 21))
        self.txt_change_pass = QLineEdit(self.groupBox)
        self.txt_change_pass.setObjectName(u"txt_change_pass")
        self.txt_change_pass.setGeometry(QRect(10, 160, 261, 21))
        self.groupBox_2 = QGroupBox(configs)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 230, 281, 131))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 53, 16))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 53, 16))
        self.txt_http = QLineEdit(self.groupBox_2)
        self.txt_http.setObjectName(u"txt_http")
        self.txt_http.setGeometry(QRect(10, 40, 261, 21))
        self.txt_https = QLineEdit(self.groupBox_2)
        self.txt_https.setObjectName(u"txt_https")
        self.txt_https.setGeometry(QRect(10, 90, 261, 21))
        self.cb_is_pring_log = QCheckBox(configs)
        self.cb_is_pring_log.setObjectName(u"cb_is_pring_log")
        self.cb_is_pring_log.setGeometry(QRect(10, 370, 281, 20))
        self.btn_save = QPushButton(configs)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(80, 410, 101, 31))
        self.tabWidget = QTabWidget(configs)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(300, 10, 541, 531))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.txt_cf_json = QTextBrowser(self.tab)
        self.txt_cf_json.setObjectName(u"txt_cf_json")
        self.txt_cf_json.setGeometry(QRect(0, 0, 531, 511))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.txt_cf_json_doc = QTextBrowser(self.tab_2)
        self.txt_cf_json_doc.setObjectName(u"txt_cf_json_doc")
        self.txt_cf_json_doc.setGeometry(QRect(0, 0, 531, 501))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(configs)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(configs)
    # setupUi

    def retranslateUi(self, configs):
        configs.setWindowTitle(QCoreApplication.translate("configs", u"\u7cfb\u7edf\u914d\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("configs", u"\u79d8\u94a5\u76f8\u5173", None))
        self.label.setText(QCoreApplication.translate("configs", u"apiKey", None))
        self.label_2.setText(QCoreApplication.translate("configs", u"secret", None))
        self.label_3.setText(QCoreApplication.translate("configs", u"\u4ea4\u6613\u5bc6\u7801", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("configs", u"\u4ee3\u7406", None))
        self.label_4.setText(QCoreApplication.translate("configs", u"http", None))
        self.label_5.setText(QCoreApplication.translate("configs", u"https", None))
        self.cb_is_pring_log.setText(QCoreApplication.translate("configs", u"\u662f\u5426\u6253\u5370http\u8bf7\u793a\u65e5\u5fd7", None))
        self.btn_save.setText(QCoreApplication.translate("configs", u"\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("configs", u"\u6240\u6709\u914d\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("configs", u"\u914d\u7f6e\u8bf4\u660e", None))
    # retranslateUi

