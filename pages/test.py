from qfluentwidgets import SimpleCardWidget,CaptionLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout


class myWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.label = CaptionLabel(self)
        self.label.setText("文本处理")

        self.v = QVBoxLayout()
        self.v.addWidget(self.label)

        self.setObjectName("test")
#
# class myCardWidget(SimpleCardWidget):
#     def __init__(self):
#         super().__init__()
