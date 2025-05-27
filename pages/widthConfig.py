from qfluentwidgets import Slider
from PySide6.QtCore import Qt


class MySlider(Slider):
    def __init__(self, orientation=Qt.Orientation.Horizontal, parent=None,value):
        super().__init__(orientation, parent)
        self.initUI(value)

    def initUI(self,value):
        # 配置滑块属性
        self.setRange(0, 1000)
        self.setValue(value)  # 默认值