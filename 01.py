from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont
from qfluentwidgets import FluentIcon as FIF
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QWidget
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QFont, QIcon

from pages.noSpace import noSpace
from pages.systemTray import TrayApp
from pages.test import myWidget


class Window(FluentWindow):
    """ 主界面 """

    def __init__(self):
        super().__init__()

        # 创建子界面，实际使用时将 Widget 换成自己的子界面
        self.noSpaceInterface = noSpace()

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.noSpaceInterface, FIF.HOME, 'test')
    def initWindow(self):
        self.resize(900, 700)
        self.setWindowTitle('小工具箱')
        self.setWindowIcon(QIcon('icons/trayIcon.png'))

    def closeEvent(self, event):
        self.hide()      # 隐藏窗口
        event.ignore()   # 忽略关闭事件，窗口不会被销毁


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    tray = TrayApp(app, w)
    w.show()
    app.exec()
