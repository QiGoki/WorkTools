from qfluentwidgets import Slider, LineEdit, CaptionLabel, ToolButton, FluentIcon, ToolTipFilter, \
    ToolTipPosition
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout


# 按钮初始化函数
def init_btn(btn, tip_text, signal_func):
    btn.setToolTip(tip_text)  # 设置提示词
    btn.setToolTipDuration(1000)  # 设置显示时间
    # 给按钮安装工具提示过滤器
    btn.installEventFilter(ToolTipFilter(btn, showDelay=300, position=ToolTipPosition.BOTTOM))
    # 按钮信号
    btn.clicked.connect(signal_func)


class Setting(QFrame):
    def __init__(self, target_widgets: [], parent=None):
        super().__init__(parent)
        # 批量保存widget
        self.sliders = []
        # reset按钮
        self.reset_btn = ToolButton(FluentIcon.BRUSH)
        # add_widget按钮
        self.add_widget_btn = ToolButton(FluentIcon.ADD)

        # 按钮布局
        self.btn_layout = QHBoxLayout()
        self.btn_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.btn_layout.addWidget(self.reset_btn)
        self.btn_layout.addWidget(self.add_widget_btn)
        # 主布局
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.btn_layout)
        self.setLayout(self.main_layout)

        self.init(target_widgets)

        self.setObjectName("setting")
    # 初始化，主要就是生生成lider
    def init(self, target_widgets):
        for widget in target_widgets:
            item = SliderItem(widget)
            self.main_layout.addWidget(item)
            self.sliders.append(item)
        # 按钮初始化
        init_btn(self.reset_btn, "重置设置", self.on_rest_btn_clicked)
        init_btn(self.add_widget_btn, "添加要调整的组件", self.on_add_btn_clicked)
        # 焦点设置到窗口
        self.setFocus()
        # 设置窗口信息
        self.setFixedWidth(550)
        self.setWindowTitle("设置")
        self.setWindowIcon(FluentIcon.SETTING.icon())

    def on_rest_btn_clicked(self):
        for slider in self.sliders:
            slider.reset()

    def on_add_btn_clicked(self):
        pass


class SliderItem(QFrame):
    def __init__(self, target_widget, parent=None):
        super().__init__(parent)
        self.init_value = 100
        self.target_widget = target_widget
        self.title = CaptionLabel(self)
        self.title.setText(target_widget.objectName())
        self.slider = Slider(Qt.Orientation.Horizontal)
        self.num_label = LineEdit()

        self.initUI(target_widget)

        self.h_box_layout = QHBoxLayout()
        self.h_box_layout.addWidget(self.title)
        self.h_box_layout.addWidget(self.slider)
        self.h_box_layout.addWidget(self.num_label)
        self.setFixedWidth(500)
        self.setLayout(self.h_box_layout)

    def initUI(self, target_widget):
        self.init_value = target_widget.width()
        # 配置标题属性
        self.title.setFixedWidth(100)
        # 配置滑块属性
        self.slider.setRange(100, 1000)
        self.slider.setValue(self.init_value)
        self.slider.setFixedWidth(300)
        # 配置输入框属性
        self.num_label.setText(str(self.init_value))
        self.num_label.setFixedWidth(50)
        # 配置信号
        self.slider.valueChanged.connect(self.on_slider_change)
        self.num_label.textEdited.connect(self.on_label_change)

    def on_slider_change(self, value):
        self.target_widget.setFixedWidth(value)
        self.num_label.setText(str(value))

    def on_label_change(self, value):
        v = int(value)
        if self.slider.minimum() <= v <= self.slider.maximum():
            self.target_widget.setFixedWidth(v)
            self.slider.setValue(v)

    # 响应reset
    def reset(self):
        self.slider.setValue(self.init_value)
        self.num_label.setText(str(self.init_value))
