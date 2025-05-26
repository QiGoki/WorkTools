from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget, QListWidgetItem
from PySide6.QtCore import Qt, QEvent

from qfluentwidgets import (TextEdit, TitleLabel, HorizontalSeparator, CommandBar, ListWidget, SubtitleLabel,
                            SimpleCardWidget, BodyLabel, CaptionLabel
                            )

from data.textProcessData import testData


class noSpace(QWidget):
    def __init__(self):
        super().__init__()
        # 标题
        self.title = TitleLabel('文字处理')
        # 分割线
        self.hSeparator = HorizontalSeparator()
        self.hSeparator.setFixedWidth(int(self.width() / 2))
        #处理部分，应该要换成列表
        self.tp = TextProcess(parent=self)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.title)
        self.vbox.addWidget(self.hSeparator)
        self.vbox.addSpacing(10)
        self.vbox.addWidget(self.tp)

        self.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.vbox)

        self.setObjectName('removeSpaces')


class TextProcess(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.list = HistoryList(self)

        self.vBoxLayout = QVBoxLayout()
        self.commandBar = CommandBar(self)
        self.textEdit = TextEdit(self)

        #左列表右处理
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(self.list)

        self.vBoxLayout.addWidget(self.commandBar)
        self.vBoxLayout.addWidget(self.textEdit)

        self.hBoxLayout.addLayout(self.vBoxLayout)
        # 一些格式设置
        self.hBoxLayout.setSpacing(10)
        self.hBoxLayout.setStretchFactor(self.list, 3)
        self.hBoxLayout.setStretchFactor(self.vBoxLayout, 6)

        self.setLayout(self.hBoxLayout)

    def initList(self):
        self.list.addItems(['1', '2', '3'])
    # def resizeEvent(self, event):
    #     if self.parent():
    #         new_width = self.parent().width() / 2
    #         self.setFixedWidth(new_width)
    #     super().resizeEvent(event)


class HistoryList(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title = SubtitleLabel(self)
        self.title.setText('历史记录')
        self.list = ListWidget(self)
        self.initList()

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.title)
        self.vBoxLayout.addWidget(self.list)

    def initList(self):
        item = QListWidgetItem()
        itemWidget = HistoryListItemCard("test", "2025-05-26")
        self.list.addItem(item)
        self.list.setItemWidget(item, itemWidget)

        item1 = QListWidgetItem()
        itemWidget = HistoryListItemCard("test", "2025-05-26")
        self.list.addItem(item1)
        self.list.setItemWidget(item1, itemWidget)


class HistoryListItemCard(SimpleCardWidget):
    def __init__(self, text, time):
        super().__init__()
        self.content = BodyLabel(self)
        self.content.setText(text)
        self.time = CaptionLabel(self)
        self.time.setText(time)

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.content)
        self.vBoxLayout.addWidget(self.time)
        self.setLayout(self.vBoxLayout)
