import XsCore
import ccxt
from PySide6.QtWidgets import QMainWindow, QWidget, QDialog
from XsCore import xsIni, XsIniUtils

from ui.sel_exchange import Ui_sel_exchange


class sel_exchange(QDialog):
    """
    如果不想使用模式对话框，可以直接使用QWidget，但QWidget只能调用show()方法打开非模式窗口
    并且需要在init里创建窗口实例，否则会闪退
    使用 QDialog 可以调用exec()方法打开模式对话框,可以在当前代码创建实例并调用exec()
    """

    def __init__(self):
        super(sel_exchange, self).__init__()
        self.ui = Ui_sel_exchange()  # QUiLoader().load('index.ui') #Ui_MainWindow()
        self.ui.setupUi(self)
        # 禁止最大化和调整窗口
        self.setFixedSize(self.width(), self.height())
        self.ui.lst_exchange.itemDoubleClicked.connect(self.add_item)
        self.ui.lst_sels.itemDoubleClicked.connect(self.del_item)
        self.ui.btn_sel.clicked.connect(self.save_exchanges)

        self.sel_items = set()
        self.load_exchange()

    def load_exchange(self):
        exs = ccxt.exchanges
        self.ui.lst_exchange.addItems(exs)

        ex_changes = xsIni.getAppValue('exchanges')
        if ex_changes != '':
            self.sel_items = set(ex_changes.split(','))
            self.ui.lst_sels.addItems(self.sel_items)

    def add_item(self, item):
        self.ui.lst_sels.clear()
        item_text = item.text()
        self.sel_items.add(item_text)
        self.ui.lst_sels.addItems(self.sel_items)

    def del_item(self, item):
        item_text = item.text()
        self.sel_items.remove(item_text)
        self.ui.lst_sels.clear()
        self.ui.lst_sels.addItems(self.sel_items)

    def save_exchanges(self):
        value = ','.join(self.sel_items)
        xsIni.setAppItem("exchanges",value)
        XsCore.showInfo('保存成功，但需要重启才能加载新数据')