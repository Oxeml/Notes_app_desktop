# initial setup test, just opens the window

from PyQt6.QtWidgets import QApplication, QWidget
import sys

# looking for a specific argument in the list of passed arguments
is_test = "--test-mode" in sys.argv

app = QApplication(sys.argv)
window = QWidget()

# test part
if is_test:
    window.setWindowTitle("test mode")
else:
    window.setWindowTitle("Your reading app")

window.show()
sys.exit(app.exec())