import XsCore
from PySide6.QtWidgets import QMainWindow, QWidget, QDialog
from XsCore import xsIni, XsIniUtils, XsFso

from ui.configs import Ui_configs
from ui.help_doc import Ui_help_doc


class HelpDoc(QWidget):
    """
    如果不想使用模式对话框，可以直接使用QWidget，但QWidget只能调用show()方法打开非模式窗口
    使用 QDialog 可以调用exec()方法打开模式对话框
    """

    def __init__(self,file_name):
        super(HelpDoc, self).__init__()
        self.ui = Ui_help_doc()  # QUiLoader().load('index.ui') #Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_data(file_name)

    def init_data(self,file_name):
        value = XsFso.readFile(f'database/plugin_help/{file_name}.md')
        self.ui.txt_doc.setMarkdown(value)

