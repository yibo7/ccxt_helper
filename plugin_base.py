from abc import ABC, abstractmethod

import ccxt
from PySide6 import QtWidgets
# import ccxt.async_support as ccxt
from XsCore import xsIni
from ccxt import Exchange


class PluginBase(ABC):
    name: str = ""
    display_name: str = ""
    info: str = ""
    help_doc = "" # 不重写为没有文档 使用文档说明，为md文件，存放database的plugin_help下

    def __init__(self):
        self.exchange: Exchange = None

    @abstractmethod
    def get_ui(self) -> QtWidgets.QVBoxLayout():
        pass

    def init_exchange(self, ex_name):
        # config = {
        #     'proxies': {
        #         'http': 'http://127.0.0.1:41081',
        #         'https': 'http://127.0.0.1:41081'
        #     },
        #     'verbose': True
        # }

        config = {}

        value = xsIni.getAppValue('api_key')
        if value != '':
            config['apiKey'] = value

        value = xsIni.getAppValue('api_secret')
        if value != '':
            config['secret'] = value

        value = xsIni.getAppValue('api_changepass')
        if value != '':
            config['password'] = value

        http = xsIni.getAppValue('daiLi_http')
        https = xsIni.getAppValue('daiLi_https')
        if http != '' and https != '':
            config['proxies'] = {
                'http': http,
                'https': https
            }

        value = xsIni.getAppBool('is_print_log')
        if value:
            config['verbose'] = True

        self.exchange: Exchange = getattr(ccxt, ex_name)(config)

