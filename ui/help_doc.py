# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_doc.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_help_doc(object):
    def setupUi(self, help_doc):
        if not help_doc.objectName():
            help_doc.setObjectName(u"help_doc")
        help_doc.resize(628, 569)
        self.verticalLayout = QVBoxLayout(help_doc)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_doc = QTextBrowser(help_doc)
        self.txt_doc.setObjectName(u"txt_doc")

        self.verticalLayout.addWidget(self.txt_doc)


        self.retranslateUi(help_doc)

        QMetaObject.connectSlotsByName(help_doc)
    # setupUi

    def retranslateUi(self, help_doc):
        help_doc.setWindowTitle(QCoreApplication.translate("help_doc", u"\u5e2e\u52a9\u6587\u6863", None))
    # retranslateUi

