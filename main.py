import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QLabel, QScrollArea, QFrame, QGridLayout)
from PyQt6.QtCore import Qt
import db
from card import NoteCard
from create_note import NewNote

class NotebookApp (QWidget):
    def __init__(self):
        super().__init__()
        db.init_db()
        self.setWindowTitle("Minimal Notes")
        self.resize(450, 600)

        self.main_layout = QVBoxLayout(self)

        # greeting element
        self.greeting = QLabel("Hello! What's on your mind today?")
        self.greeting.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.greeting.setStyleSheet("font-size: 18px; margin: 10px")

        self.main_layout.addWidget(self.greeting)

        # add note button
        self.add_btn = QPushButton("+ New Note")
        self.add_btn.setMinimumHeight(40)
        self.add_btn.clicked.connect(self.open_new_note)
        self.main_layout.addWidget(self.add_btn)

        # scroll area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QGridLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll.setWidget(self.scroll_content)
        self.main_layout.addWidget(self.scroll)

        self.load_notes()

    def load_notes(self):
        # clear what's already there
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)

        notes = db.get_notes()
        columns_count = 3

        for index, note in enumerate(notes):
            n_id, n_title, n_time = note

            btn = QPushButton(f"{n_title}\n{n_time}")
            btn.setFixedSize(130, 100)
            btn.clicked.connect(lambda checked, id=n_id: self.open_existing_note(id))

            row = index // columns_count
            col = index % columns_count

            self.scroll_layout.addWidget(btn, row, col)


    def open_new_note(self):
        self.new_win = NewNote()

        # usage of custom signal to update notes list
        self.new_win.note_saved.connect(self.load_notes)

        self.new_win.show()


    def open_existing_note(self, note_id):
        data = db.get_note_by_id(note_id)
        self.edit_win = NoteCard(title = data[1], body = data[2], note_id = data[0])
        
        #usage of custom signal to update notes list
        self.edit_win.note_edited_saved.connect(self.load_notes)
        self.edit_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = NotebookApp()
    demo.show()
    sys.exit(app.exec())
