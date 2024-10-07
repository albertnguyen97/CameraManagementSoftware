from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QSize(1200, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")

        # Using QTabWidget instead of QTabBar
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)  # Set tabs on the left (vertical)
        self.tabWidget.setObjectName("tabWidget")

        # Live Page
        self.widgetLive = QWidget()
        self.widgetLive.setObjectName("widgetLive")

        # Create a vertical layout for widgetLive
        self.liveLayout = QVBoxLayout(self.widgetLive)

        # Create a horizontal layout for tab bar and add button
        self.tabBarLayout = QHBoxLayout()

        # Create a QTabWidget for the Live page tabs
        self.tabWidgetLive = QTabWidget(self.widgetLive)
        self.tabWidgetLive.setTabsClosable(True)  # Allow closing tabs
        self.tabWidgetLive.setMovable(True)  # Allow moving tabs

        # Add default tab
        self.addLiveTab("Tab 1")

        # Connect signal for closing tabs
        self.tabWidgetLive.tabCloseRequested.connect(self.closeLiveTab)

        # Button to add new tabs (place this beside the tabWidgetLive)
        self.addTabButton = QPushButton("+", self.widgetLive)
        self.addTabButton.setFixedSize(30, 30)  # Set size for the button
        self.addTabButton.clicked.connect(self.addNewTab)

        # Add the tabWidget and button to the horizontal layout
        self.tabBarLayout.addWidget(self.tabWidgetLive)
        self.tabBarLayout.addWidget(self.addTabButton)

        # Add the horizontal layout to the liveLayout
        self.liveLayout.addLayout(self.tabBarLayout)

        # Add the widgetLive to the tabWidget
        self.tabWidget.addTab(self.widgetLive, "Live")

        # Record Page
        self.widgetRecord = QWidget()
        self.widgetRecord.setObjectName("widgetRecord")
        self.tabWidget.addTab(self.widgetRecord, "Record")

        # Location Page
        self.widgetDevice = QWidget()
        self.widgetDevice.setObjectName("widgetLocation")
        self.tabWidget.addTab(self.widgetDevice, "Location")

        # User Page
        self.widgetUser = QWidget()
        self.widgetUser.setObjectName("widgetUser")
        self.tabWidget.addTab(self.widgetUser, "User")

        # Settings Page
        self.widgetSettings = QWidget()
        self.widgetSettings.setObjectName("widgetSettings")
        self.tabWidget.addTab(self.widgetSettings, "Settings")

        self.mainLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.applyStyles()

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def applyStyles(self):
        # Apply style for the entire application
        self.centralwidget.setStyleSheet("background-color: #F5F5F5;")

        # Style for the tabWidget
        self.tabWidget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid lightgray;
            }
            QTabBar::tab {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                margin: 2px;
                border-radius: 5px;
                min-width: 50px;
                font-size: 16px;
            }
            QTabBar::tab:selected {
                background-color: Green;
            }
            QTabBar::tab:hover {
                background-color: #3e8e41;
            }
        """)

        # Style for the stacked widget pages
        page_style = """
            QWidget {
                background-color: #FFFFFF;
                border: 1px solid #E0E0E0;
                border-radius: 10px;
            }
        """
        self.widgetUser.setStyleSheet(page_style)
        self.widgetRecord.setStyleSheet(page_style)
        self.widgetDevice.setStyleSheet(page_style)
        self.widgetSettings.setStyleSheet(page_style)
        self.widgetLive.setStyleSheet(page_style)

    def addLiveTab(self, title):
        """Add a new tab in the Live section with a TreeWidget on the left"""
        newTab = QWidget()
        tabLayout = QHBoxLayout(newTab)
        sideTabLayout = QVBoxLayout(newTab)
        lineEdit = QLineEdit(newTab)
        lineEdit.setFixedSize(300,30)
        # Add QTreeWidget on the left side of the tab
        tree_widget = QTreeWidget(newTab)
        tree_widget.setHeaderLabels(['Family Tree'])
        tree_widget.setFixedSize(300,10000)
        tree_widget.setHeaderLabel(f"Tree {title}")
        # Thêm thế hệ đầu tiên (Grandparents)
        self.populateTreeWidget(tree_widget)
        tree_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        tree_widget.customContextMenuRequested.connect(lambda pos: self.showContextMenu(tree_widget, pos))

        sideTabLayout.addWidget(lineEdit)
        sideTabLayout.addWidget(tree_widget)
        tabLayout.addLayout(sideTabLayout)
        # Add content on the right side
        label = QLabel(f"Content of {title}", newTab)
        tabLayout.addWidget(label)

        self.tabWidgetLive.addTab(newTab, title)
    def populateTreeWidget(self, tree_widget):
        """Populate tree widget with initial items"""
        # Add first generation (Grandparents)
        grandparent = QTreeWidgetItem(tree_widget)
        grandparent.setText(0, 'Grandparents')
        grandparent.setFlags(grandparent.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        grandparent.setCheckState(0, Qt.CheckState.Unchecked)

        # Add second generation (Parents)
        parent1 = QTreeWidgetItem(grandparent)
        parent1.setText(0, 'Parent 1')
        parent1.setFlags(parent1.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        parent1.setCheckState(0, Qt.CheckState.Unchecked)

        parent2 = QTreeWidgetItem(grandparent)
        parent2.setText(0, 'Parent 2')
        parent2.setFlags(parent2.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        parent2.setCheckState(0, Qt.CheckState.Unchecked)

        # Add third generation (Children)
        child1 = QTreeWidgetItem(parent1)
        child1.setText(0, 'Child 1')
        child1.setFlags(child1.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        child1.setCheckState(0, Qt.CheckState.Unchecked)

        child2 = QTreeWidgetItem(parent1)
        child2.setText(0, 'Child 2')
        child2.setFlags(child2.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        child2.setCheckState(0, Qt.CheckState.Unchecked)

        child3 = QTreeWidgetItem(parent2)
        child3.setText(0, 'Child 3')
        child3.setFlags(child3.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        child3.setCheckState(0, Qt.CheckState.Unchecked)

        child4 = QTreeWidgetItem(parent2)
        child4.setText(0, 'Child 4')
        child4.setFlags(child4.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        child4.setCheckState(0, Qt.CheckState.Unchecked)


    def showContextMenu(self, tree_widget, pos):
        """Show context menu for adding and removing items"""
        menu = QMenu(tree_widget)

        add_action = QAction("Add", tree_widget)
        add_action.triggered.connect(lambda: self.addTreeItem(tree_widget))
        menu.addAction(add_action)

        remove_action = QAction("Remove", tree_widget)
        remove_action.triggered.connect(lambda: self.removeTreeItem(tree_widget))
        menu.addAction(remove_action)

        menu.exec(tree_widget.viewport().mapToGlobal(pos))

    def addTreeItem(self, tree_widget):
        """Add a new item to the tree widget and allow renaming"""
        current_item = tree_widget.currentItem()
        if not current_item:
            current_item = tree_widget.invisibleRootItem()  # Add to root if no item is selected

        new_item = QTreeWidgetItem(current_item)
        new_item.setText(0, 'New Item')
        new_item.setFlags(new_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        new_item.setCheckState(0, Qt.CheckState.Unchecked)

        # Gọi hộp thoại nhập tên mới
        self.change_item_name(tree_widget)

    def change_item_name(self, tree_widget):
        pass
        # """Change the name of the newly added item"""
        # current_item = tree_widget.currentItem()
        # if current_item:
        #     new_name, ok = QInputDialog.getText(self, "Change Item Name", "Enter new name:", text=current_item.text(0))
        #     if ok and new_name:
        #         current_item.setText(0, new_name)

    def removeTreeItem(self, tree_widget):
        """Remove the selected item from the tree widget"""
        current_item = tree_widget.currentItem()
        if current_item:
            index = tree_widget.indexOfTopLevelItem(current_item)
            if index != -1:
                tree_widget.takeTopLevelItem(index)  # Remove from root level
            else:
                parent = current_item.parent()
                if parent:
                    parent.removeChild(current_item)  # Remove from parent



    def addNewTab(self):
        """Handler for adding a new tab when the button is clicked"""
        tabCount = self.tabWidgetLive.count() + 1
        self.addLiveTab(f"Tab {tabCount}")

    def closeLiveTab(self, index):
        """Handler for closing tabs"""
        if self.tabWidgetLive.count() > 1:  # Ensure at least one tab remains
            self.tabWidgetLive.removeTab(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.applyStyles()
    MainWindow.show()
    sys.exit(app.exec())
