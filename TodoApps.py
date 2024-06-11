import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget
from PyQt5 import QtCore, QtGui

class TodoApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('To-Do App')
        self.setGeometry(100,100,400,300)

        #List to store input tasks
        self.tasks = []

        #Define layout
        self.layout = QVBoxLayout()

        #Define input field, list, and buttons
        self.input_field = QLineEdit()
        self.add_button = QPushButton('Add Task')
        self.remove_button = QPushButton('Remove Task')
        self.task_list = QListWidget(self)

        #Add input field, list, and add/remove button widgets
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.task_list)

        #On click add or remove task is called
        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)

        self.setLayout(self.layout)
    
    def remove_task(self):
        #remove list item from list widget
        listItems = self.task_list.selectedItems()
        if not listItems: return
        for item in listItems:
            self.task_list.takeItem(self.task_list.row(item))

    def add_task(self):
        #Adding item to list widget
        task = self.input_field.text()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.input_field.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())