import json

import pandas as pd
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QSizePolicy, QHeaderView
from ccxt import Exchange, NetworkError

from pandas_model import PandasModel
from plugin_base import PluginBase
from plugin_ui_base import PluginUiBase


class TickData_XsPlugin(PluginBase):
    name: str = "TickData"
    display_name: str = "实时行情"
    info = "调用方法:exchange.fetch_ticker(),点击交易对更新或每1秒更新一次"
    help_doc = 'tick_data'

    def get_ui(self) -> QtWidgets.QVBoxLayout():
        return TickDataUi(self.exchange)


class TickDataUi(PluginUiBase):
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

    def __init__(self, ex):
        super().__init__(ex)

        self.vbox = QtWidgets.QHBoxLayout()
        self.setLayout(self.vbox)
        self.listWidget = QtWidgets.QListWidget()

        self.tv_bid = QtWidgets.QTextBrowser()

        self.vbox.addWidget(self.listWidget)
        self.vbox.addWidget(self.tv_bid)
        # self.vbox.addWidget(self.json_box)

        self.listWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.listWidget.itemClicked.connect(self.clicked)
        self.symbol = ''
        # 初始化一个定时器
        self.timer = QTimer(self)
        # 定义时间超时连接start_app
        self.timer.timeout.connect(self.update_book)
        # 定义时间任务是一次性任务
        # self.timer.setSingleShot(True)
        # 启动时间任务
        self.timer.start(1000)

    def closeEvent(self, event):
        print('关闭了...')
        self.timer.stop()
        event.accept()
        self.destroy()
        # event.ignore()

    def clicked(self, item):
        self.symbol = item.text()
        self.update_book()

    key_cn = {
        "ask": '卖一价',
        "askVolume": '卖一价对应的量',
        "average": '平均价格',
        "baseVolume": '24小时基准货币的成交量',
        "bid": '买一价',
        "bidVolume": '买一价对应的数量',
        "change": '当前价与开盘价差',
        "close": '当前价',
        "datetime": "时间",
        "high": '24小时最高价',
        "last": '最后成交价',
        "low": '24小时最低价',
        "open": '24小时前第一分钟开盘价',
        "percentage": '差价百分比',
        "previousClose": '上根K线的收盘价',
        "quoteVolume": "24小时内报价货币的成交量",
        "symbol": "交易对称号",
        "timestamp": '时间戳',
        "vwap": '交易成本'
    }

    def update_book(self):
        if self.symbol == '':
            return
        try:
            data = self.exchange.fetch_ticker(self.symbol,limit=100)  # fetch_tickers
            del data['info']
            contents = []
            for key, value in data.items():
                contents.append(f'【{self.key_cn[key]}】 = {value}      --{key}')
            self.tv_bid.setText('\n'.join(contents))

        except NetworkError as err:
            self.on_log(f'请示Api无法响应：{err}', is_json=False)
            return
        self.on_log(data)
