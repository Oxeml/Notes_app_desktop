from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import pyqtSignal
import sys
import db

class NewNote(QWidget):
    # defining a signal
    note_saved = pyqtSignal()

    # main logic for the Class
    def __init__(self):
        super().__init__()
        
        # 1. Definig the visual elemnts of the card
        # title field
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("note Title")

        # note body input area
        self.body_input = QTextEdit(self)
        self.body_input.setPlaceholderText("What's on your mind today?")
        self.body_input.setFixedSize(400, 400)

        # 3. save button, close button
        self.save_button = QPushButton("save note")
        self.close_button = QPushButton("discard")

        # 2. Creating a container with a layout to hold
        # all visual elements
        self.setWindowTitle("New amazing note")
        self.layout = QVBoxLayout(self)

        # 3. Creating a container for buttons
        self.btn_widget = QWidget()
        btn_layout = QHBoxLayout(self.btn_widget)
        btn_layout.addWidget(self.save_button)
        btn_layout.addWidget(self.close_button)
        
        # 3. adding the elements to the layout
        self.layout.addWidget(self.title_input)
        self.layout.addWidget(self.body_input)
        self.layout.addWidget(self.btn_widget)

        # 4. signals and slots
        self.close_button.clicked.connect(self.close)
        self.save_button.clicked.connect(self.save_note_to_db)

    # 5. Method to save the new note to a database
    def save_note_to_db(self):
        t = self.title_input.text()
        b = self.body_input.toPlainText()

        if t.strip() == "" and b.strip() == "":
            return
            
        db.add_note(t, b)

        # trigger the signal to reload (update) all notes
        # later in the main
        self.note_saved.emit()

        # close the window for a new note (by that time notes already updated)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    card = NewNote()
    card.show()
    sys.exit(app.exec())
        

