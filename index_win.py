import asyncio
import threading
from importlib import import_module

import XsCore
import ccxt
import pyperclip
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow

from sub_wins.configs import CongisWin
from sub_wins.help_doc import HelpDoc
from sub_wins.sel_exchange import sel_exchange
from ui.index import Ui_MainWindow
from XsCore import XsPath, xsIni


class IndexWindow(QMainWindow):

    def __init__(self):
        super(IndexWindow, self).__init__()
        self.ui = Ui_MainWindow()  # QUiLoader().load('index.ui') #Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listWidget.itemClicked.connect(self.clicked)
        self.init_combobox()
        self.plugin_ui = QtWidgets.QLabel("...")
        # self.ui.layout_main.addWidget(self.plugin_widget)
        self.plugins = []
        self.plugin = None
        self.load_plugins()
        self.ui.btn_copy.clicked.connect(self.btn_copy_onclick)
        self.ui.btn_sel_exchange.clicked.connect(self.btn_sel_exchange_click)
        self.ui.btn_helper.clicked.connect(self.open_doc)
        # self.ui.action_configs.clicked.connect(self.open_configs)
        # self.sub_sel_exchange = sel_exchange()

        # 在代码里添加工具栏
        self.toolbar = self.addToolBar('config')
        cfAction = QAction(QIcon('images/1.png'), '系统配置', self)
        cfAction.setShortcut('Ctrl+S')
        cfAction.triggered.connect(self.open_configs)
        self.toolbar.addAction(cfAction)

        # 初始化一个定时器
        self.timer = QTimer(self)
        # 定义时间超时连接start_app
        self.timer.timeout.connect(self.show_log)
        # 定义时间任务是一次性任务
        # self.timer.setSingleShot(True)
        # 启动时间任务
        self.timer.start(1000)
        self.ui.btn_helper.hide()
        self.doc_win = None

    def open_doc(self):
        if self.plugin:
            self.doc_win = HelpDoc(self.plugin.help_doc)
            self.doc_win.show()

    def open_configs(self):
        sub = CongisWin()
        sub.exec()

    def btn_sel_exchange_click(self):
        sub = sel_exchange()
        sub.exec()

    def btn_copy_onclick(self):
        txt = self.ui.textBrowser.toPlainText()
        pyperclip.copy(txt)
        XsCore.showInfo("已经复制到剪切板")

    def init_combobox(self):
        # self.ui.comboBox.currentIndexChanged.connect(self.selectionChange)  # 获取当前选中元素的索引 并按照指定格式输出
        exs = ccxt.exchanges
        ex_changes = xsIni.getAppValue('exchanges')
        if ex_changes != '':
            exs = set(ex_changes.split(','))
        self.ui.comboBox.addItems(exs)
        self.ui.comboBox.activated.connect(self.cb_change)  # 获取当前选中元素的索引

    def cb_change(self, index):
        pass
        # self.exchange_name = self.ui.comboBox.currentText()

    def load_plugins(self):

        files = XsPath.getSubFiles("plugins")
        for file in files:
            m_path = file.replace('\\', '.')
            m_path = m_path.replace('.py', '')
            module = import_module(m_path)
            for name in dir(module):
                if name.endswith('_XsPlugin'):
                    plugin_class = getattr(module, name)
                    self.plugins.append(plugin_class())

        for plugin in self.plugins:
            self.ui.listWidget.addItem(plugin.display_name)
            # print(plugin().get_name())

    # def on_log(self, log):
    #     self.ui.txt_log.setText(log)

    def show_log(self):
        if hasattr(self.plugin_ui, 'logs') and len(self.plugin_ui.logs) > 0:
            log = self.plugin_ui.logs.pop()
            self.ui.textBrowser.setText(log)
        # 如果要在多线程的情况更新QLabel这样的控件，可以直接使用threading或threading.Timer
        # 但要在多线程里更新QLabel之外的控制往往会出错，所以要使用以三种方式
        # 1.利用计时器模块QTimer
        # 2.使用多线程模块QThread
        # 3.使用事件处理功能

        # t = threading.Timer(1, self.show_log)
        # t.start()

    def clicked(self, item):
        index = self.ui.listWidget.currentIndex().row()
        self.plugin = self.plugins[index]
        if self.plugin.help_doc != '':
            self.ui.btn_helper.show()
        else:
            self.ui.btn_helper.hide()

        exchange_name = self.ui.comboBox.currentText()
        self.plugin.init_exchange(exchange_name)
        self.plugin_ui.close()
        self.ui.layout_main.removeWidget(self.plugin_ui)

        self.ui.lbPluginName.setText(self.plugin.display_name)
        self.ui.lbPluginInfo.setText(self.plugin.info)
        self.plugin_ui = self.plugin.get_ui()
        self.ui.layout_main.addWidget(self.plugin_ui)
        t = threading.Thread(target=self.plugin_ui.data_bind, )  # args=(i,)
        t.start()
