import XsCore
from PySide6.QtWidgets import QMainWindow, QWidget, QDialog
from XsCore import xsIni, XsIniUtils, XsFso

from ui.configs import Ui_configs


class CongisWin(QDialog):
    """
    如果不想使用模式对话框，可以直接使用QWidget，但QWidget只能调用show()方法打开非模式窗口
    使用 QDialog 可以调用exec()方法打开模式对话框
    """

    def __init__(self):
        super(CongisWin, self).__init__()
        self.ui = Ui_configs()  # QUiLoader().load('index.ui') #Ui_MainWindow()
        self.ui.setupUi(self)
        # 禁止最大化和调整窗口
        self.setFixedSize(self.width(), self.height())
        # self.ui.lst_exchange.itemDoubleClicked.connect(self.add_item)
        # self.ui.lst_sels.itemDoubleClicked.connect(self.del_item)
        self.ui.btn_save.clicked.connect(self.save_configs)
        self.init_configs()



    def init_configs(self):
        value = xsIni.getAppValue('api_key')
        self.ui.txt_api_key.setText(value)

        value = xsIni.getAppValue('api_secret')
        self.ui.txt_secret.setText(value)

        value = xsIni.getAppValue('api_changepass')
        self.ui.txt_change_pass.setText(value)

        value = xsIni.getAppValue('daiLi_http')
        self.ui.txt_http.setText(value)

        value = xsIni.getAppValue('daiLi_https')
        self.ui.txt_https.setText(value)

        value = xsIni.getAppBool('is_print_log')
        self.ui.cb_is_pring_log.setChecked(value)

        value = XsFso.readFile('database/configinfo.txt')

        self.ui.txt_cf_json.setText(value)

        value = XsFso.readFile('database/configinfodoc.md')

        self.ui.txt_cf_json_doc.setMarkdown(value)



    def save_configs(self):
        value = self.ui.txt_api_key.text()
        xsIni.setAppItem("api_key", value)

        value = self.ui.txt_secret.text()
        xsIni.setAppItem("api_secret", value)

        value = self.ui.txt_change_pass.text()
        xsIni.setAppItem("api_changepass", value)

        value = self.ui.txt_http.text()
        xsIni.setAppItem("daiLi_http", value)

        value = self.ui.txt_https.text()
        xsIni.setAppItem("daiLi_https", value)

        value = self.ui.cb_is_pring_log.isChecked()
        xsIni.setAppItem("is_print_log", str(value))

        XsCore.showInfo('保存成功')
