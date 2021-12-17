import asyncio
import json
import threading

from PySide6 import QtWidgets
from PySide6.QtWidgets import QSizePolicy
from ccxt.async_support import Exchange

from plugin_base import PluginBase
from plugin_ui_base import PluginUiBase


class AllMarkets_XsPlugin(PluginBase):
    name: str = "AllMarkets"
    display_name: str = "市场数据结构"
    info = "查看交易符号和市场ID，调用方法:exchange.load_markets(),并从返回的字典获取某个KEY下的详情"
    help_doc = "allmarkets"

    def get_ui(self) -> QtWidgets.QVBoxLayout():
        return AllMarketsUi(self.exchange)


class AllMarketsUi(PluginUiBase):

    def __init__(self, ex):
        """"""
        super().__init__(ex)

        self.vbox = QtWidgets.QHBoxLayout()

        self.setLayout(self.vbox)
        self.listWidget = QtWidgets.QListWidget()
        self.json_box = QtWidgets.QTextBrowser()
        self.vbox.addWidget(self.listWidget)
        self.vbox.addWidget(self.json_box)

        self.listWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.listWidget.itemClicked.connect(self.clicked)
        self.on_log('数据加载中...', is_json=False)

    def data_bind(self):
        markets = self.exchange.load_markets()

        # for key in markets:
        #     self.listWidget.addItem(key)
        self.on_log(markets)
        lstSort = []
        for key in markets:
            lstSort.append(key)
        lstSort.sort()
        self.listWidget.addItems(lstSort)

    # dicKeyInfo = {
    #
    # }
    def clicked(self, item):
        data = self.exchange.markets[item.text()]
        self.on_log(data)
        js = json.dumps(data, indent=4, sort_keys=True)

        self.json_box.setText(js)
