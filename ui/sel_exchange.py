# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sel_exchange.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_sel_exchange(object):
    def setupUi(self, sel_exchange):
        if not sel_exchange.objectName():
            sel_exchange.setObjectName(u"sel_exchange")
        sel_exchange.resize(315, 299)
        self.verticalLayout = QVBoxLayout(sel_exchange)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(sel_exchange)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(sel_exchange)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lst_exchange = QListWidget(sel_exchange)
        self.lst_exchange.setObjectName(u"lst_exchange")

        self.horizontalLayout.addWidget(self.lst_exchange)

        self.lst_sels = QListWidget(sel_exchange)
        self.lst_sels.setObjectName(u"lst_sels")

        self.horizontalLayout.addWidget(self.lst_sels)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn_sel = QPushButton(sel_exchange)
        self.btn_sel.setObjectName(u"btn_sel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sel.sizePolicy().hasHeightForWidth())
        self.btn_sel.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_sel)


        self.retranslateUi(sel_exchange)

        QMetaObject.connectSlotsByName(sel_exchange)
    # setupUi

    def retranslateUi(self, sel_exchange):
        sel_exchange.setWindowTitle(QCoreApplication.translate("sel_exchange", u"\u9009\u62e9\u5e38\u7528\u4ea4\u6613\u6240", None))
        self.label_2.setText(QCoreApplication.translate("sel_exchange", u"\u5f85\u9009\uff08\u53cc\u51fb\u9009\u62e9\uff09", None))
        self.label.setText(QCoreApplication.translate("sel_exchange", u"\u5df2\u9009\uff08\u53cc\u51fb\u79fb\u9664\uff09", None))
        self.btn_sel.setText(QCoreApplication.translate("sel_exchange", u"\u786e\u8ba4", None))
    # retranslateUi

