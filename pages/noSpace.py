from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt,QEvent

from qfluentwidgets import (TextEdit,TitleLabel,HeaderCardWidget,PushButton,ToolButton,FluentIcon,CardWidget,IconWidget,
BodyLabel,CaptionLabel,TransparentToolButton)


class NoSpace(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.textEdit = TextFrame(self)
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.textEdit)

        # 必须给子界面设置全局唯一的对象名
        self.setObjectName('removeSpaces')


class TextFrame(HeaderCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle('文本栏')

        self.vbox = QVBoxLayout()
        # 文本框
        self.textEdit = TextEdit()
        self.textEdit.setObjectName('myTextEdit')
        self.hbox = QHBoxLayout()
        self.doButton = PushButton("确定")
        self.clearButton = ToolButton(FluentIcon.SETTING,self)
        self.hbox.addWidget(self.doButton)
        self.hbox.addWidget(self.clearButton)

        self.test = TextEdit()
        self.vbox.addWidget(self.textEdit)
        self.vbox.addWidget(self.test)
        self.vbox.addLayout(self.hbox)

        self.viewLayout.addLayout(self.vbox)

class AppCard(CardWidget):

    def __init__(self, title, content, parent=None):
        super().__init__(parent)
        self.iconWidget = IconWidget(FluentIcon.HOME,self)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.openButton = PushButton('Open', self)
        self.moreButton = TransparentToolButton(FluentIcon.MORE, self)
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(73)
        self.iconWidget.setFixedSize(48, 48)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")
        self.openButton.setFixedWidth(120)

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.openButton, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignRight)

        self.moreButton.setFixedSize(32, 32)


        # 必须给子界面设置全局唯一的对象名
        self.setObjectName('removeSpaces')
