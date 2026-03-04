import sys
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QLabel, QScrollArea, QFrame, QGridLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import db
from card import NoteCard
from create_note import NewNote

# helper function to convert a relative path into an absolute
# path, so that when executable is installed neccessary items
# will be accessed.
def resource_path(relative_path):
    if hasattr (sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
class NotebookApp (QWidget):
    def __init__(self):
        super().__init__()
        db.init_db()
        self.setWindowTitle("My Notes ✌️")
        self.setWindowIcon(QIcon(resource_path("./assets/icons/rocket-lunch.png")))
        self.setFixedSize(450, 600)

        self.main_layout = QVBoxLayout(self)

        # greeting element
        self.greeting = QLabel("Hello! What's on your mind today?")
        self.greeting.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.greeting.setStyleSheet("font-size: 18px; margin: 10px")
        self.greeting.setObjectName("Greeting") # for styling

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

        # styling link
        self.load_stylesheet()
        
        self.load_notes()

    def load_stylesheet(self):
        try:
            with open(resource_path("styles.qss"), "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("Style file not found!")

    def load_notes(self):
        # clear what's already there
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)

        notes = db.get_notes()
        columns_count = 3

        for index, note in enumerate(notes):
            n_id, n_title, n_time = note

            if len(n_title) > 9:
                display_title = n_title[:9] + ".."
            else:
                display_title = n_title

            dispaly_day = n_time[:10]
            display_time = n_time[11:16] 
            btn = QPushButton(f"{display_title}\n\n{dispaly_day}\n{display_time}")
            btn.setObjectName("NoteCardBtn")
            btn.setFixedSize(130, 130)
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

        # usage of a signal when a note is deleted
        self.edit_win.note_deleted.connect(self.load_notes)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = NotebookApp()
    demo.show()
    sys.exit(app.exec())
