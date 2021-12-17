import sys

import ccxt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from index_win import IndexWindow

if __name__ == '__main__':
    print(dir(ccxt.hitbtc))  # Python
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('ui/logo.ico'))
    indexWin = IndexWindow()
    indexWin.show()
    sys.exit(app.exec())