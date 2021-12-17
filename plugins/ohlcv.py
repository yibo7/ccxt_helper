import json

import pandas as pd
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QSizePolicy, QHeaderView
from ccxt import Exchange, NetworkError

from pandas_model import PandasModel
from plugin_base import PluginBase
from plugin_ui_base import PluginUiBase


class OHLCV_XsPlugin(PluginBase):
    name: str = "OHLCV"
    display_name: str = "获取K线数据"
    info = "调用方法:exchange.fetch_ohlcv()"
    help_doc = 'order_books'

    def get_ui(self) -> QtWidgets.QVBoxLayout():
        return OrderBooksUi(self.exchange)


class OrderBooksUi(PluginUiBase):
    def data_bind(self):
        self.on_log('数据加载中...', is_json=False)
        try:
            markets = self.exchange.load_markets()
            self.on_log(markets)
        except NetworkError as err:
            self.on_log(f'请示Api无法响应：{err}', is_json=False)
            return

        lstSort = []
        for key in markets:
            lstSort.append(key)
        lstSort.sort()
        self.listWidget.addItems(lstSort)
        # for key in markets:
        #     self.listWidget.addItem(key)

    def __init__(self, ex):
        super().__init__(ex)

        self.vbox = QtWidgets.QHBoxLayout()
        self.setLayout(self.vbox)
        self.listWidget = QtWidgets.QListWidget()
        # self.json_box = QtWidgets.QTextBrowser()
        self.tv_data = QtWidgets.QTableView()
        self.tv_data.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.vbox.addWidget(self.listWidget)
        self.vbox.addWidget(self.tv_data)

        self.listWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.listWidget.itemClicked.connect(self.clicked)
        self.symbol = ''
        # # 初始化一个定时器
        # self.timer = QTimer(self)
        # # 定义时间超时连接start_app
        # self.timer.timeout.connect(self.update_book)
        # # 定义时间任务是一次性任务
        # # self.timer.setSingleShot(True)
        # # 启动时间任务
        # self.timer.start(3000)

    def closeEvent(self, event):
        print('关闭了...')
        # self.timer.stop()
        event.accept()
        self.destroy()
        # event.ignore()

    def clicked(self, item):
        self.symbol = item.text()
        self.update_book()

    def update_book(self):
        if self.symbol == '':
            return
        try:
            data = self.exchange.fetch_ohlcv(self.symbol)  # fetch_order_book ,fetch_l2_order_book
        except NetworkError as err:
            self.on_log(f'请示Api无法响应：{err}', is_json=False)
            return
            # js = json.dumps(data, indent=4, sort_keys=True)
        self.on_log(data)
        data_ask = pd.DataFrame(data, columns=["时间戳", "开盘价格O", "最高价格H", "最低价格L",  "收盘价格C","交易量V"])
        model = PandasModel(data_ask)
        self.tv_data.setModel(model)

