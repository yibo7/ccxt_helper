import datetime
import os
import shutil
import threading
import time
from datetime import date, timedelta

import XsCore
import json

import pandas as pd
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QSizePolicy, QHeaderView
from XsCore import XsDateUtils
from ccxt import Exchange, NetworkError

from pandas_model import PandasModel
from plugin_base import PluginBase
from plugin_ui_base import PluginUiBase


class Out_Ohlcv_XsPlugin(PluginBase):
    name: str = "Out_Ohlcv"
    display_name: str = "导出历史K线"
    info = "调用方法:exchange.fetch_ohlcv(symbol, timeframe='1m', since=start_time_stamp, limit=limit_count)"

    def get_ui(self) -> QtWidgets.QVBoxLayout():
        return OrderBooksUi(self.exchange)


class OrderBooksUi(PluginUiBase):
    kline_type = {
        '分钟': '1m',
        '小时': '1h',
        '天': '1d',
    }

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
        self.v_right = QtWidgets.QVBoxLayout()

        self.vbox.addWidget(self.listWidget)
        self.vbox.addLayout(self.v_right)

        self.v_right.addWidget(QtWidgets.QLabel('选择K线类型'))
        self.cb_k_type = QtWidgets.QComboBox()
        self.cb_k_type.addItems(self.kline_type.keys())
        self.v_right.addWidget(self.cb_k_type)

        self.v_right.addWidget(QtWidgets.QLabel('选择开始日期'))
        self.dt_start = QtWidgets.QDateEdit()
        to_date = date.today()
        to_date += timedelta(days=-7)
        self.dt_start.setDate(to_date)
        self.v_right.addWidget(self.dt_start)

        self.v_right.addWidget(QtWidgets.QLabel('选择结束日期'))
        self.dt_end = QtWidgets.QDateEdit()
        self.dt_end.setDate(date.today())
        self.v_right.addWidget(self.dt_end)

        self.btn_sel_path = QtWidgets.QPushButton("选择保存目录")
        self.btn_sel_path.clicked.connect(self.sel_path)
        self.v_right.addWidget(self.btn_sel_path)

        self.btn_save = QtWidgets.QPushButton("导出")
        self.btn_save.clicked.connect(self.start_run)
        self.v_right.addWidget(self.btn_save)

        self.listWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.listWidget.itemClicked.connect(self.clicked)
        self.symbol = ''
        self.out_path = '' # 用户选择的最终整合导出目录
        self.save_dir = "" # 保存临时数据目录
        self.startTime = ""
        self.endTime = ""
        self.timeType = ""

    def sel_path(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        self.out_path = directory
        self.btn_sel_path.setText(directory)

    def start_run(self):
        if self.symbol == '':
            XsCore.showInfo('请先选择交易对')
            return
        if self.out_path == '':
            XsCore.showInfo('请选择导出目录')
            return

        self.timeType = self.cb_k_type.currentText()
        self.startTime = self.dt_start.date().toString(Qt.ISODate)
        self.endTime = self.dt_end.date().toString(Qt.ISODate)
        self.btn_save.setEnabled(False)
        thread_bind = threading.Thread(target=self.get_kline,args=(self.symbol, self.startTime, self.endTime,self.kline_type[self.timeType]))  # args=(i,)
        thread_bind.start()
        # self.get_kline(self.symbol, s, e,self.kline_type[kl_type_key])

    def get_kline(self, symbol, start_time, end_time,date_type = '1m'):
        """
        爬取交易所数据的方法.
        :param date_type:
        :param symbol: 请求的symbol: like BTC/USDT, ETH/USD等。
        :param start_time: like 2018-1-1
        :param end_time: like 2019-1-1
        :return:
        """
        current_path = os.getcwd()
        file_dir = os.path.join(current_path,'database\\out', symbol.replace('/', ''))

        if os.path.exists(file_dir):
            # 如果目录存在，需要先删除，这样可以先清空目录下的数据.
            shutil.rmtree(file_dir) # 对非空目录的删除要使用 shutil.rmtree，而os.removedirs 只能删除空目录
            print("删除目录")

        os.makedirs(file_dir) # 创建这个文件夹，用来存放临时数据
        self.save_dir = file_dir
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d')
        end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')

        start_time_stamp = int(time.mktime(start_time.timetuple())) * 1000
        end_time_stamp = int(time.mktime(end_time.timetuple())) * 1000

        limit_count = 200  # bybit 请求的数据有限制，每次只能请求200个.
        self.on_log('开始获取数据...', is_json=False)
        while True:
            try:
                print(f'从开始时间：{start_time_stamp}开始请求{limit_count}条数据')
                data = self.exchange.fetch_ohlcv(symbol, timeframe=date_type, since=start_time_stamp, limit=limit_count)
                df = pd.DataFrame(data)
                df.rename(columns={0: 'datetime', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'},
                          inplace=True)

                start_time_stamp = int(df.iloc[-1]['datetime'])  # 获取下一个次请求的时间.
                filename = str(start_time_stamp) + '.csv'
                save_file_path = os.path.join(file_dir, filename)

                df.set_index('datetime', drop=True, inplace=True)
                df.to_csv(save_file_path)
                # self.on_log(f'保存成功:{save_file_path}', is_json=False)
                if start_time_stamp > end_time_stamp:
                    print("完成数据的请求.")
                    # self.on_log('完成数据的请求', is_json=False)
                    break

                time.sleep(0.2)  # 1/25

            except Exception as error:
                print("发生错误了：")
                print(error)
                time.sleep(10)
        print("清洗数据.")
        self.clear_datas()
        print("结束.")
        self.on_log('所有操作完成！', is_json=False)
        self.btn_save.setEnabled(True)

    def closeEvent(self, event):
        print('当前插件关闭...')
        # self.timer.stop()
        event.accept()
        self.destroy()
        # event.ignore()

    def clicked(self, item):
        self.symbol = item.text()

    def sample_datas(self):
        """
        :param exchange_name:
        :param symbol:
        :return:
        """
        path = self.save_dir
        file_paths = []
        for root, dirs, files in os.walk(path):
            if files:
                for file in files:
                    if file.endswith('.csv'):
                        file_paths.append(os.path.join(path, file))

        file_paths = sorted(file_paths)
        all_df = pd.DataFrame()

        for file in file_paths:
            df = pd.read_csv(file)
            # all_df = all_df.append(df, ignore_index=True)
            all_df = pd.concat([all_df,df], ignore_index=True)

        all_df = all_df.sort_values(by='datetime', ascending=True)

        # print(all_df)

        return all_df

        # for index, item in all_df.iterrows():
        #     try:
        #         dt = (pd.to_datetime(item['open_time'], unit='ms'))
        #         print(dt)
        #         dt = datetime.datetime.strptime(str(dt), '%Y-%m-%d %H:%M:%S')  # 2018-01-01 17:36:00:42
        #         print(dt)
        #     except:
        #         dt = (pd.to_datetime(item['open_time'], unit='ms'))
        #         print(dt)

    def clear_datas(self):
        df = self.sample_datas()
        # print(df)
        # exit()
        # df['open_time'] = df['open_time'].apply(lambda x: time.mktime(x.timetuple()))
        # # 日期.timetuple() 这个用法 通过它将日期转换成时间元组
        # # print(df)
        # df['open_time'] = df['open_time'].apply(lambda x: (x // 60) * 60 * 1000)
        df['datetime'] = df['datetime'].apply(lambda x: (x // 60) * 60)  # 获取整分的数据.
        print(df)
        df['Datetime2'] = pd.to_datetime(df['datetime'], unit='ms') + pd.Timedelta(hours=8)  # 把UTC时间转成北京时间.
        df['Datetime2'] = df['Datetime2'].apply(lambda x: str(x)[0:19])  # 2018-11-15 00:47:0034, 通过截取字符串长度.
        # df['Datetime3'] = XsDateUtils.seconds_to_str(df['datetime'].astype(int)/1000)
        df.drop_duplicates(subset=['datetime'], inplace=True)
        df.set_index('Datetime2', inplace=True)
        # print("*" * 20)
        # print(df)
        savetodir = f'{self.out_path}/{self.symbol.replace("/","")}从{self.startTime}到{self.endTime}的{self.timeType}线.csv'
        print(savetodir)
        df.to_csv(savetodir)

