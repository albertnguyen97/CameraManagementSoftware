import sys
from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class TreeWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo QTreeWidget
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(['Family Tree'])

        # Thêm thế hệ đầu tiên (Grandparents)
        grandparent = QTreeWidgetItem(self.tree_widget)
        grandparent.setText(0, 'Grandparents')
        grandparent.setFlags(grandparent.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        grandparent.setCheckState(0, Qt.CheckState.Unchecked)

        # Thêm thế hệ thứ hai (Parents)
        parent1 = QTreeWidgetItem(grandparent)
        parent1.setText(0, 'Parent 1')
        parent1.setFlags(parent1.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        parent1.setCheckState(0, Qt.CheckState.Unchecked)

        parent2 = QTreeWidgetItem(grandparent)
        parent2.setText(0, 'Parent 2')
        parent2.setFlags(parent2.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        parent2.setCheckState(0, Qt.CheckState.Unchecked)

        # Thêm thế hệ thứ ba (Children)
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

        # Thiết lập layout
        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)
        self.setLayout(layout)

        self.setWindowTitle("Family Tree with Checkboxes")
        self.setGeometry(100, 100, 400, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TreeWidgetDemo()
    demo.show()
    sys.exit(app.exec())





