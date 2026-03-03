from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit, QVBoxLayout
import sys

# creating widgets that can be imported from the file
def create_note_widgets():
    title_input = QLineEdit()
    title_input.setPlaceholderText("note title")

    body_input = QTextEdit()
    body_input.setPlaceholderText("What's on your mind today?")
    body_input.setFixedSize(300, 300)

    edit_button = QPushButton("edit note")

    return title_input, body_input, edit_button


# this part ensures a separate window is spawn only in cas
# the file is run directly
# in case of import from the file it won't open a window
# and run the code

if __name__ == "__main__":
    app = QApplication(sys.argv)
    title, body, edit_button = create_note_widgets()

    window = QWidget()
    window.setMinimumSize(370, 370)
    window.setWindowTitle("A Note")

    layout = QVBoxLayout()
    layout.addWidget(title)
    layout.addWidget(body)
    layout.addWidget(edit_button)

    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())