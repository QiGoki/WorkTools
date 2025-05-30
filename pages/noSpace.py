from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget, QListWidgetItem
from PySide6.QtCore import Qt, QEvent, QSize

from qfluentwidgets import (TextEdit, TitleLabel, HorizontalSeparator, CommandBar, ListWidget, SubtitleLabel,
                            SimpleCardWidget, BodyLabel, CaptionLabel, SearchLineEdit, Action, Slider
                            )

from data.textProcessData import fakeData
from pages.Setting import Setting


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

        # self.history_sb = MySlider(self.tp.historyListArea,"historyListArea")
        # self.vbox.addWidget(self.history_sb)

class TextProcess(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.historyListArea = HistoryList(self)
        self.historyListArea.setObjectName("historyListArea")

        self.vBoxLayout = QVBoxLayout()
        self.commandBar = CommandBar(self)
        self.textEdit = TextEdit(self)
        #左列表右处理
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(self.historyListArea)

        self.vBoxLayout.addWidget(self.commandBar)
        self.vBoxLayout.addWidget(self.textEdit)

        self.hBoxLayout.addLayout(self.vBoxLayout)
        # 一些格式设置
        self.hBoxLayout.setSpacing(10)

        self.setLayout(self.hBoxLayout)


class HistoryList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #标题
        self.title = SubtitleLabel(self)
        self.title.setText('历史记录')
        #搜索框
        self.searchLineEdit = SearchLineEdit(self)
        self.initSearch()
        #列表

        # 创建父容器并设置样式
        self.listBox = SimpleCardWidget(self)
        self.listBox.setObjectName("listBox")
        self.list = ListWidget(self.listBox)
        self.list.setObjectName("list")
        self.listLayout = QVBoxLayout(self.listBox)
        self.listLayout.addWidget(self.list)
        self.listLayout.setContentsMargins(5, 0, 0, 0)
        self.initList()
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.title)
        self.vBoxLayout.addWidget(self.searchLineEdit)
        self.vBoxLayout.addWidget(self.listBox)
        self.setFixedWidth(350)
        self.setLayout(self.vBoxLayout)


    def initList(self):
        self.list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        for i in fakeData:
            item = QListWidgetItem()
            itemWidget = HistoryListItemCard(i["content"], i["date"])
            item.setSizeHint(itemWidget.size())
            self.list.addItem(item)
            self.list.setItemWidget(item, itemWidget)
    def initSearch(self):
        self.action = Action()
        self.searchLineEdit.setPlaceholderText("可按内容或时间搜索")
        # self.searchLineEdit.addAction()


class HistoryListItemCard(SimpleCardWidget):
    def __init__(self, text, time):
        super().__init__()
        # 内容
        self.content = text
        # 用于展示的部分，大于20就加“... ...”
        self.display = BodyLabel(self)
        self.setDisplay()
        self.time = CaptionLabel(self)
        self.time.setText(time)

        self.time.setStyleSheet("color: #cccccc;")

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.display)
        self.vBoxLayout.addWidget(self.time, alignment=Qt.AlignmentFlag.AlignRight)
        self.setFixedSize(305, 60)
        self.setLayout(self.vBoxLayout)

    def setDisplay(self):
        if len(self.content) >21:
            self.display.setText(self.content[:20]+"...")