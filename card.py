from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout
import sys

class NoteCard(QWidget):
    #__init__() - is a Python class constructor
    # super().__init__() - to call a parent class' (QWidget) constructor
    # Python convention - to declare all variables in __init__
    def __init__(self, title="New Note", body=""):
        super().__init__()
        self.saved_title = title
        self.saved_body = body

        self.init_ui()
        self.set_view_mode() #default mode

    # set up initial card window
    def init_ui(self):
        self.setWindowTitle("Your Note")
        self.layout = QVBoxLayout(self)

        # fields
        self.title_input = QLineEdit(self.saved_title, self)
        self.body_input = QTextEdit(self.saved_body, self)
        self.body_input.setFixedSize(300, 300)

        # view mode layout
        self.view_widget = QWidget()
        view_layout = QHBoxLayout(self.view_widget)
        self.edit_btn = QPushButton("Edit")
        self.close_btn = QPushButton("Close")
        view_layout.addWidget(self.edit_btn)
        view_layout.addWidget(self.close_btn)

        # edit mode layout
        self.edit_widget = QWidget()
        edit_layout = QHBoxLayout(self.edit_widget)
        self.save_btn = QPushButton("Save")
        self.discard_btn = QPushButton("Discard")
        edit_layout.addWidget(self.save_btn)
        edit_layout.addWidget(self.discard_btn)


        # main layout
        self.layout.addWidget(self.title_input)
        self.layout.addWidget(self.body_input)
        self.layout.addWidget(self.view_widget)
        self.layout.addWidget(self.edit_widget)

        # connect signals and slots
        self.edit_btn.clicked.connect(self.set_edit_mode)
        self.close_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.save_changes)
        self.discard_btn.clicked.connect(self.discard_changes)

    # method for initial view mode
    def set_view_mode(self):
        self.title_input.setReadOnly(True)
        self.body_input.setReadOnly(True)
        self.view_widget.show()
        self.edit_widget.hide()
        
    # methods for slots
    # 1. method for edit mode
    def set_edit_mode(self):
        self.title_input.setReadOnly(False)
        self.body_input.setReadOnly(False)
        self.view_widget.hide()
        self.edit_widget.show()

    # 2. Save_changes mode
    def save_changes(self):
        self.saved_title = self.title_input.text()
        self.saved_body = self.body_input.toPlainText()
        self.set_view_mode()

    # 3. Discard changes
    def discard_changes(self):
        self.title_input.setText(self.saved_title)
        self.body_input.setText(self.saved_body)
        self.set_view_mode()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    card = NoteCard("Mood", "Feeling melancholic")
    card.show()
    sys.exit(app.exec())

