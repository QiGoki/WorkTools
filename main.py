import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QFileDialog, QListWidgetItem)
from qfluentwidgets import (MSFluentWindow, FluentIcon, setTheme, Theme,
                            PrimaryPushButton, ListWidget, ImageLabel,
                            CaptionLabel, BodyLabel, LineEdit)


class ChatBubble(BodyLabel):
    def __init__(self, text: str, is_user: bool, parent=None):
        super().__init__(text, parent)
        self.is_user = is_user
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignRight if is_user else Qt.AlignmentFlag.AlignLeft)
        self.setProperty("isUser", is_user)
        self.setStyleSheet("""
            ChatBubble[isUser="true"] {
                background: #0078d4;
                color: white;
                border-radius: 8px;
                padding: 8px 12px;
                margin: 4px 0;
                max-width: 70%;
            }
            ChatBubble[isUser="false"] {
                background: #f0f0f0;
                color: black;
                border-radius: 8px;
                padding: 8px 12px;
                margin: 4px 0;
                max-width: 70%;
            }
        """)


class MainWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()
        setTheme(Theme.LIGHT)
        self.setWindowTitle("Image Assistant")
        self.resize(1200, 800)

        # 主界面初始化（关键修复点）
        self.mainInterface = QWidget()
        self.mainInterface.setObjectName("mainInterface")  # 添加objectName
        self.initLayout()
        self.initWidgets()

        # 添加主界面到导航
        self.addSubInterface(self.mainInterface, FluentIcon.HOME, "Main")

    def initLayout(self):
        self.mainLayout = QHBoxLayout(self.mainInterface)
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.mainLayout.setSpacing(20)

        # 左侧布局（图片区域）
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setSpacing(15)

        # 右侧布局（对话区域）
        self.rightLayout = QVBoxLayout()
        self.rightLayout.setSpacing(15)

        self.mainLayout.addLayout(self.leftLayout, 4)
        self.mainLayout.addLayout(self.rightLayout, 6)

    def initWidgets(self):
        # 图片显示区域
        self.imageLabel = ImageLabel(self.mainInterface)
        self.imageLabel.setBorderRadius(8, 8, 8, 8)
        self.imageLabel.setMinimumSize(400, 400)
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imageLabel.setText("Click to upload image")

        # 上传按钮
        self.uploadBtn = PrimaryPushButton("Upload Image", self.mainInterface)
        self.uploadBtn.setIcon(FluentIcon.PHOTO)
        self.uploadBtn.clicked.connect(self.openImage)

        # 预设按钮组
        self.presetLayout = QHBoxLayout()
        self.presetBtn1 = PrimaryPushButton("Preset 1", self.mainInterface)
        self.presetBtn2 = PrimaryPushButton("Preset 2", self.mainInterface)
        self.configBtn = PrimaryPushButton(FluentIcon.SETTING, "")
        self.presetLayout.addWidget(self.presetBtn1)
        self.presetLayout.addWidget(self.presetBtn2)
        self.presetLayout.addWidget(self.configBtn)

        # 左侧布局组装
        self.leftLayout.addWidget(self.imageLabel)
        self.leftLayout.addLayout(self.presetLayout)
        self.leftLayout.addWidget(self.uploadBtn)

        # 对话列表
        self.chatList = ListWidget(self.mainInterface)
        self.chatList.setStyleSheet("background: transparent;")
        self.chatList.setSpacing(10)

        # 输入区域
        self.inputLayout = QHBoxLayout()
        self.inputField = LineEdit()
        self.sendBtn = PrimaryPushButton("Send", self.mainInterface)
        self.inputLayout.addWidget(self.inputField)
        self.inputLayout.addWidget(self.sendBtn)

        # 右侧布局组装
        self.rightLayout.addWidget(CaptionLabel("Conversation"))
        self.rightLayout.addWidget(self.chatList)
        self.rightLayout.addLayout(self.inputLayout)

        # 信号连接
        self.sendBtn.clicked.connect(self.sendMessage)
        self.presetBtn1.clicked.connect(lambda: self.sendPreset("Preset 1 query"))
        self.presetBtn2.clicked.connect(lambda: self.sendPreset("Preset 2 query"))

    def openImage(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if path:
            self.showImage(path)

    def showImage(self, path):
        pixmap = QPixmap(path)
        scaled_pixmap = pixmap.scaled(
            self.imageLabel.width(), self.imageLabel.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setImage(scaled_pixmap)

    def sendMessage(self):
        text = self.inputField.text().strip()
        if not text:
            return

        self.addUserMessage(text)
        self.inputField.clear()
        self.simulateModelResponse(text)

    def sendPreset(self, text):
        self.addUserMessage(text)
        self.simulateModelResponse(text)

    def addUserMessage(self, text):
        bubble = ChatBubble(text, True)
        item = QListWidgetItem()
        item.setSizeHint(bubble.sizeHint())
        self.chatList.addItem(item)
        self.chatList.setItemWidget(item, bubble)
        self.chatList.scrollToBottom()

    def addBotMessage(self, text):
        bubble = ChatBubble(text, False)
        item = QListWidgetItem()
        item.setSizeHint(bubble.sizeHint())
        self.chatList.addItem(item)
        self.chatList.setItemWidget(item, bubble)
        self.chatList.scrollToBottom()

    def simulateModelResponse(self, query):
        response = f"Response to: {query}\nThis is a sample answer from AI."
        self.addBotMessage(response)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 强制设置字体解决警告
    app.setStyleSheet("""
    * {
        font-family: Arial;
        font-size: 13px;
    }
    QMessageBox {
        font-family: Arial;
    }
    """)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())