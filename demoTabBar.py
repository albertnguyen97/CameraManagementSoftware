import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QTabBar, QToolButton
)
from PyQt6.QtCore import Qt

class TabExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStackedWidget Example")
        self.setGeometry(100, 100, 600, 400)

        # Tạo QStackedWidget để chứa các trang (giống như nội dung của các tab)
        self.stacked_widget = QStackedWidget(self)

        # Tạo QTabBar để hiển thị các tab
        self.tab_bar = QTabBar(self)
        self.tab_bar.setTabsClosable(True)
        self.tab_bar.tabCloseRequested.connect(self.close_tab)
        self.tab_bar.currentChanged.connect(self.switch_tab)

        # Thêm tab đầu tiên
        self.add_tab()

        # Nút thêm tab
        self.add_tab_button = QToolButton(self)
        self.add_tab_button.setText("+")
        self.add_tab_button.clicked.connect(self.add_tab)

        # Tạo layout cho tab bar và nút thêm tab
        tab_layout = QHBoxLayout()
        tab_layout.addWidget(self.tab_bar)
        tab_layout.addWidget(self.add_tab_button)

        # Tạo widget để chứa layout tab bar và stacked widget
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        main_layout.addLayout(tab_layout)
        main_layout.addWidget(self.stacked_widget)

        self.setCentralWidget(main_widget)

    def add_tab(self):
        # Số thứ tự của tab mới
        index = self.tab_bar.count() + 1

        # Tạo một trang mới cho QStackedWidget
        new_page = QWidget()
        layout = QVBoxLayout(new_page)
        layout.addWidget(QLabel(f"This is Tab {index}"))
        new_page.setLayout(layout)

        # Thêm trang vào QStackedWidget
        self.stacked_widget.addWidget(new_page)

        # Thêm một tab mới vào QTabBar
        self.tab_bar.addTab(f"Tab {index}")

        # Chuyển tới tab mới
        self.tab_bar.setCurrentIndex(self.tab_bar.count() - 1)

    def close_tab(self, index):
        if self.tab_bar.count() > 1:  # Không cho phép đóng tab cuối cùng
            self.tab_bar.removeTab(index)
            widget_to_remove = self.stacked_widget.widget(index)
            self.stacked_widget.removeWidget(widget_to_remove)

    def switch_tab(self, index):
        # Chuyển đổi trang hiển thị theo tab được chọn
        self.stacked_widget.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabExample()
    window.show()
    sys.exit(app.exec())
