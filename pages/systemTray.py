from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from PySide6.QtGui import QIcon, QAction,QCursor
from PySide6.QtCore import QObject, Qt

from qfluentwidgets import Flyout, InfoBarIcon, FlyoutAnimationType

from methods import text_strip


class TrayApp(QObject):
    def __init__(self, app, main_window):
        super().__init__()
        self.app = app
        self.main_window = main_window  # 直接绑定已有的主窗口实例

        # 创建系统托盘图标，使用系统主题图标或本地图标
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon.fromTheme("edit-paste"))
        self.tray.setToolTip("小工具合集")  # 设置托盘图标的提示文本

        # 创建托盘菜单
        self.menu = QMenu()

        # 添加“打开主界面”菜单项，并绑定显示主窗口的方法
        self.action_show = QAction("打开主界面")
        self.action_show.triggered.connect(self.show_main_window)
        self.menu.addAction(self.action_show)

        # 添加“删除空格”菜单项，并绑定删除空格的方法（暂未实现）
        self.action_del_space = QAction("文本处理")
        self.action_del_space.triggered.connect(self.delete_spaces)
        self.menu.addAction(self.action_del_space)

        # 菜单分隔线
        self.menu.addSeparator()

        # 添加“退出”菜单项，并绑定退出方法
        self.action_quit = QAction("退出")
        self.action_quit.triggered.connect(self.quit)
        self.menu.addAction(self.action_quit)

        # 设置托盘图标的右键菜单 会有bug
        self.tray.setContextMenu(self.menu)
        # 连接托盘图标的点击等激活事件
        # self.tray.activated.connect(self.on_tray_activated)

        # 显示托盘图标
        self.tray.show()

    def on_tray_activated(self, reason):
        """
        托盘图标被激活（点击/双击等）时的处理。
        Trigger 通常是单击，DoubleClick 是双击。
        在这两种情况下弹出菜单。
        """
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            # 在托盘图标中心弹出菜单（可根据平台适当调整弹出位置）
            self.menu.popup(self.tray.geometry().center())

    def show_main_window(self):
        """
        显示主窗口，并将其置顶、激活。
        """
        self.main_window.setWindowState(
            self.main_window.windowState() & ~Qt.WindowState.WindowMinimized | Qt.WindowState.WindowActive
        )
        self.main_window.show()
        self.main_window.raise_()
        self.main_window.activateWindow()

    def quit(self):
        """
        退出应用程序前，先隐藏托盘图标，再退出主程序。
        """
        self.tray.hide()
        self.app.quit()

    def delete_spaces(self):
        """
        获取剪贴板内容，调用相关函数，再放回剪贴板。
        """
        clipboard = QApplication.clipboard()  # 获取剪贴板对象
        text = clipboard.text()  # 获取剪贴板文本内容
        text = text_strip.all_func(text)  # 调用功能函数
        clipboard.setText(text)  # 设置回剪贴板
        self.showFlyout(QCursor.pos())  # 弹窗提示

    # def showFlyout(self):
    #     Flyout.create(
    #         icon=InfoBarIcon.SUCCESS,
    #         title='',
    #         content="处理成功",
    #         target=self.menu,
    #         parent=self.menu,
    #         # isClosable=True,
    #         aniType=FlyoutAnimationType.PULL_UP
    #     )
    def showFlyout(self, position):
        flyout = Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title='',
            content="处理成功",
            target=self.tray.geometry().center(),
            parent=self.menu,
            aniType=FlyoutAnimationType.NONE
        )