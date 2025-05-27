import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton,
                               QVBoxLayout, QHBoxLayout, QMenu)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QFont,QAction


class SearchBox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # 创建主布局
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 创建下拉菜单按钮
        self.dropdown_btn = QPushButton("全部")
        self.dropdown_btn.setObjectName("dropdownButton")
        self.dropdown_btn.setMinimumHeight(30)
        self.dropdown_btn.setFlat(True)
        self.dropdown_btn.setMenu(self.createMenu())

        # 创建搜索输入框
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("搜索...")
        self.search_input.setObjectName("searchInput")
        self.search_input.setMinimumHeight(30)

        # 创建搜索按钮
        self.search_btn = QPushButton("搜索")
        self.search_btn.setObjectName("searchButton")
        self.search_btn.setMinimumHeight(30)
        self.search_btn.setCursor(Qt.PointingHandCursor)
        self.search_btn.clicked.connect(self.onSearch)

        # 添加到布局
        layout.addWidget(self.dropdown_btn)
        layout.addWidget(self.search_input, 1)  # 让输入框占据剩余空间
        layout.addWidget(self.search_btn)

        # 设置样式表
        self.setStyleSheet("""
            #dropdownButton {
                border: 1px solid #ccc;
                border-right: none;
                border-radius: 4px 0 0 4px;
                padding: 0 10px;
                background-color: #f5f5f5;
                text-align: left;
            }
            #dropdownButton::menu-indicator {
                subcontrol-position: center right;
                right: 5px;
            }
            #searchInput {
                border: 1px solid #ccc;
                border-left: none;
                border-right: none;
                padding: 0 5px;
            }
            #searchButton {
                border: 1px solid #ccc;
                border-left: none;
                border-radius: 0 4px 4px 0;
                padding: 0 15px;
                background-color: #f5f5f5;
            }
            #searchButton:hover {
                background-color: #e0e0e0;
            }
            #dropdownButton:hover, #searchInput:hover {
                border-color: #aaa;
            }
            #dropdownButton:focus, #searchInput:focus, #searchButton:focus {
                outline: none;
                border-color: #888;
            }
        """)

    def createMenu(self):
        """创建下拉菜单内容"""
        menu = QMenu(self)

        # 添加菜单项
        menu.addAction("全部", lambda: self.setFilter("全部"))
        menu.addAction("图片", lambda: self.setFilter("图片"))
        menu.addAction("视频", lambda: self.setFilter("视频"))
        menu.addAction("文档", lambda: self.setFilter("文档"))
        menu.addAction("音乐", lambda: self.setFilter("音乐"))

        return menu

    def setFilter(self, filter_text):
        """设置当前筛选条件"""
        self.dropdown_btn.setText(filter_text)

    def onSearch(self):
        """执行搜索操作"""
        search_text = self.search_input.text()
        filter_type = self.dropdown_btn.text()
        print(f"搜索: {filter_type} - {search_text}")


# 使用示例
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 确保中文显示正常
    font = QFont("SimHei")
    app.setFont(font)

    window = QWidget()
    layout = QVBoxLayout(window)
    layout.setContentsMargins(20, 20, 20, 20)

    # 添加搜索框
    search_box = SearchBox()
    layout.addWidget(search_box)

    # 添加一些间距
    layout.addStretch(1)

    window.setWindowTitle("搜索框示例")
    window.resize(500, 200)
    window.show()

    sys.exit(app.exec_())