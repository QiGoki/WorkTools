from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QComboBox, QGroupBox,
    QListWidget, QListWidgetItem, QLineEdit
)
import sys

# 单个历史记录项，自定义Widget
class HistoryItemWidget(QWidget):
    def __init__(self, content, time_str):
        super().__init__()
        layout = QHBoxLayout(self)
        content_edit = QLineEdit(content)
        content_edit.setReadOnly(True)
        time_label = QLabel(time_str)
        layout.addWidget(content_edit)
        layout.addWidget(time_label)

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文本处理工具")

        # 顶部：左-标题，右-下拉框+按钮
        top_layout = QHBoxLayout()
        title_label = QLabel("文本处理工具")
        top_layout.addWidget(title_label)
        top_layout.addStretch()
        combo = QComboBox()
        combo.addItems(["选项1", "选项2"])
        action_button = QPushButton("操作")
        top_layout.addWidget(combo)
        top_layout.addWidget(action_button)

        # 中部：左-文本编辑框，右-历史记录区
        mid_layout = QHBoxLayout()
        text_edit = QTextEdit()

        # 历史记录组
        history_group = QGroupBox("历史记录")
        history_layout = QVBoxLayout(history_group)
        history_list = QListWidget()

        # 示例：添加几个历史记录项
        for i in range(5):
            item = QListWidgetItem()
            widget = HistoryItemWidget(f"内容 {i+1}", f"2024-06-09 12:0{i}")
            item.setSizeHint(widget.sizeHint())
            history_list.addItem(item)
            history_list.setItemWidget(item, widget)

        history_layout.addWidget(history_list)
        history_group.setLayout(history_layout)

        # 布局左右区
        mid_layout.addWidget(text_edit, 2)
        mid_layout.addWidget(history_group, 1)

        # 总体布局
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(top_layout)
        main_layout.addLayout(mid_layout)

        self.setLayout(main_layout)

        # 必须给子界面设置全局唯一的对象名
        self.setObjectName('removeSpaces')
