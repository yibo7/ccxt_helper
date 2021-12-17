import json
from abc import ABC, abstractmethod

from PySide6 import QtWidgets
from ccxt import Exchange


class PluginUiBase(QtWidgets.QWidget):
    def __init__(self, ex):
        """"""
        super().__init__()
        self.exchange: Exchange = ex

    logs = []

    @abstractmethod
    def data_bind(self):
        pass

    def on_log(self, log, is_json=True):
        if is_json:
            js = json.dumps(log, indent=4, sort_keys=True)
            self.logs.append(js)
        else:
            self.logs.append(log)
        # if self.log_fun:
        #     if is_json:
        #         js = json.dumps(log, indent=4, sort_keys=True)
        #         self.log_fun(js)
        #         self.logs.append(js)
        #     else:
        #         self.log_fun(log)
        #         self.logs.append(log)
