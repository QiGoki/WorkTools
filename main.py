import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QTreeWidget,
                               QTreeWidgetItem, QVBoxLayout, QWidget, QDialog, QRadioButton, QGroupBox, QLineEdit,
                               QLabel)
from PySide6.QtCore import Qt
from qfluentwidgets import TreeWidget, MessageBoxBase,StrongBodyLabel


class ControlTreeViewer(MessageBoxBase):
    """显示widget控件树的对话框"""

    def __init__(self, parent_widget, parent):
        super().__init__(parent)
        self.title = StrongBodyLabel("控件树查看器")

        # 创建树状列表
        self.tree_widget = TreeWidget()
        self.tree_widget.setHeaderLabels(["控件类型", "ObjectName", "文本内容", "位置"])

        # 构建控件树
        self.build_control_tree(parent_widget)

        # 设置布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.title)
        layout.addWidget(self.tree_widget)
        self.viewLayout.addLayout(layout)
        self.widget.setMinimumWidth(700)
        # 展开所有节点
        self.tree_widget.expandAll()

    def build_control_tree(self, parent_widget, parent_item=None):
        """递归构建控件树"""
        # 创建当前控件的树节点
        widget_info = [
            parent_widget.__class__.__name__,
            parent_widget.objectName() or "(未设置)",
            self._get_widget_text(parent_widget) or "(无文本)",
            f"({parent_widget.x()}, {parent_widget.y()})"
        ]

        if parent_item is None:
            # 根节点
            tree_item = QTreeWidgetItem(self.tree_widget, widget_info)
        else:
            # 子节点
            tree_item = QTreeWidgetItem(parent_item, widget_info)

        # 存储widget引用以便后续操作(可选)
        tree_item.setData(0, Qt.UserRole, parent_widget)
        tree_item.setFlags(Qt.ItemFlag.ItemIsEditable)
        # 递归添加所有子控件
        for child in parent_widget.findChildren(QWidget):
            self.build_control_tree(child, tree_item)

    def _get_widget_text(self, widget):
        """获取控件的文本内容(如果有)"""
        if hasattr(widget, 'text') and callable(widget.text):
            return widget.text()
        elif hasattr(widget, 'toPlainText') and callable(widget.toPlainText):
            return widget.toPlainText()
        return None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("控件树演示")
        self.resize(800, 600)

        # 创建中央部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建示例控件
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.show_control_tree)
        layout.addWidget(self.add_button)

        # 添加一些其他控件用于演示
        label = QLabel("示例标签")
        layout.addWidget(label)

        edit = QLineEdit("示例输入框")
        layout.addWidget(edit)

        group_box = QGroupBox("分组框")
        group_layout = QVBoxLayout()
        group_box.setLayout(group_layout)

        radio1 = QRadioButton("选项1")
        radio2 = QRadioButton("选项2")
        group_layout.addWidget(radio1)
        group_layout.addWidget(radio2)

        layout.addWidget(group_box)

    def show_control_tree(self):
        """显示控件树对话框"""
        # 获取当前点击的按钮作为根控件
        sender = self.sender()

        # 创建并显示控件树对话框
        dialog = ControlTreeViewer(sender.parent(),self)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



def build_control_tree(self, target_widget):
    """递归构建控件树"""
    # 创建当前控件的树节点
    widget_info = [
        target_widget.__class__.__name__,
        target_widget.objectName() or "(未设置)",
        self._get_widget_text(target_widget) or "(无文本)",
        f"({target_widget.x()}, {target_widget.y()})"
        ]

    if target_widget.parent() is None:
        # 根节点
        tree_item = QTreeWidgetItem(self.tree_widget, widget_info)
    else:
        # 子节点
        tree_item = QTreeWidgetItem(parent_item, widget_info)

for child in parent_widget.findChildren(QWidget):
    self.build_control_tree(child, tree_item)