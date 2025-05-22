from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QEvent

from qfluentwidgets import (TextEdit, TitleLabel, HeaderCardWidget, PushButton, ToolButton, FluentIcon,
                            HeaderCardWidget, IconWidget,
                            BodyLabel, StrongBodyLabel, CommandBar)


class noSpace(QWidget):
    def __init__(self):
        super().__init__()
        self.card = AppCard(parent=self)

        self.setObjectName('removeSpaces')


class AppCard(HeaderCardWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("文字处理")

        self.vBoxLayout = QVBoxLayout()

        self.commandBar = CommandBar(self)

        self.textEdit = TextEdit(self)

        self.vBoxLayout.addWidget(self.commandBar)
        self.vBoxLayout.addWidget(self.textEdit)
        self.setContentsMargins(10,10,10,10)

        self.viewLayout.addLayout(self.vBoxLayout)
        # 必须给子界面设置全局唯一的对象名

    # def resizeEvent(self, event):
    #     if self.parent():
    #         new_width = self.parent().width() / 2
    #         self.setFixedWidth(new_width)
    #     super().resizeEvent(event)