# practicing layout for my main window

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QTextEdit
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setMinimumSize(500, 500)
window.setWindowTitle("Note Entry Window")

layout = QVBoxLayout()

# -------creating widgets---------
# 1. title field
title_input = QLineEdit()
title_input.setPlaceholderText("note title")

# 2. note input area
body_input = QTextEdit()
body_input.setPlaceholderText("What's on your mind today?")
body_input.setFixedSize(400, 400)

# 3. save button
save_button = QPushButton("save note")

#-------adding widgets to  layout --------
# otherwise they stay invisible

layout.addWidget(title_input)
layout.addWidget(body_input)
layout.addWidget(save_button)


#---------attach layout to window------
window.setLayout(layout)

window.show()
sys.exit(app.exec())