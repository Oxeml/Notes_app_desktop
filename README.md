## Notes App
Scope: to build a simple Desktop note application, not dependent on browser.
It needs to be very user-friendly, target audience is early teens.
No HTML/CSS/JS here.

## Building timeline 

### 1. Setup
- create a virtual environment in the project directory (I work with Windows and VisualStudio):
```python -m venv venv```
A folder 'venv' should appear with 'Scripts' folder inside it, which contains script for the activation.
Next we need to activate.
This needs to be done for every new project to avoid any dependency conflicts. 
```venv\Scripts\activate ```

- install dependencies and outout the list to the requirements.txt
```pip install PyQt6```
```pip install pyinstaller```
```pip freeze > requirements.txt```

- optional check that python is there
```python -c "import sys; print(sys.executable)"```
it returns the path to the pyhton executable, in my case:
```C:\Projects\notes_app\venv\Scripts\python.exe```

- optional check for the dependencies installation:
```pip list```

### Check that we can run the app and it opens a window

```from PyQt6.QtWidgets import QApplication, QWidget```
````import sys```

```app = QApplication(sys.argv)```
```window = QWidget()```
```window.show()```
```app.exec()```

when running it should open a window

### 2. Creating a DataBase with sqlite3
- Database: SQLite
- Language: Python
- Database connection handled using context managers (with sqlite3.connect(...))


This project implements basic CRUD functionality using SQLite and Python.

🟢 Create

Adds a new note to the database.

```add_note(title, content)```

SQL used:
```INSERT INTO notes (title, content) VALUES (?, ?)```

🔵 Read

Retrieves notes from the database.
```get_notes()```

SQL used:
```SELECT * FROM notes```

For a specific note:
```get_note_by_id(note_id)```
returns a single note or None if not found

SQL used:
```SELECT * FROM notes WHERE id = ?```

🟡 Update

Updates an existing note.
```update_note(note_id, title, content)```

SQL used:
```UPDATE notes```
```SET title = ?, content = ?```
```WHERE id = ?```

🔴 Delete

Removes a note from the database.
```delete_note(note_id)```

SQL used:
```DELETE FROM notes WHERE id = ?```

Initial crud tests are located in crud_tests.py, the script is executed by calling
```python crud_tests.py```


### Working with SQLite Parameters in Python
- When using cursor.execute(), dynamic values should be passed as a tuple or list (the second argument) to prevent SQL injection.
- ```cursor.execute()``` takes two arguments:
1) an SQL string itself: ```"SELECT id, title... FROM notes..."```
2) optional second argument in case of a placeholder (?) usage:
```"SELECT ... WHERE id = ?"```
- second argument should be a list or a tuple, so to pass one item as a tuple, we need to add a comma:
```cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))```

### 3. UI with PyQt
Why PyQt?

This is my first experience working with PyQt. My goal was to develop a browser-independent application, only desktop version. I found out that PyQt
simplifies the process.

- native window behavior, no need for browser engine;
- single language stack - both backend and UI is built in Python;
- easier database management, with less secuirity browser-related restrictions;
- fast (in theory) GUI prototyping, detailed documentation and tutorials with code snippets to get you started are availiable (https://doc.qt.io/).

Why it was difficult for me: I got lost in the endless list of Qt classes.

### 3.1 GUI overview
It's a note writing app, with basic CRUD functionality, so the main function is to add a new note. This is done by filling the "title" and "body" areas which are located on the upper part of the window. Bottom part contains all previously created notes, presented as small cards, 5 cards in a row. In case there are many notes the user can scroll the main window  down.

Each note card is clickable and extends in a pop up and provides functionality for editind, saving changes, closing without saving, and a note deletion.

### Applicaion Architecture

This project uses PyQt to build a graphical interface. The framework provides different application classes depending on the project's needs:
- QApplication (GUI): It initializes the window system and manages the visual theme.
- QCoreApplication (Non-GUI): Used for background services or console tools that do not require a window.

It is nicely described here, in PyQt docs: https://doc.qt.io/qt-6/qapplication.html#:~:text=It%20initializes%20the%20application%20with,the%20user%20interface%20are%20created.

This project will have a GUI, so I use QApplication.

Next question was to use QMainWindow or a QWidget.
- QWidget is a parent class of every visible object in Qt (buttons, labels, windows).
It has no built-in "spots" for standard desktop features. So like a blank canvas
- QMainWindow is a specialized widget designed to be the "Main Window" of a professional desktop app. It has built-in spots, full description and code snippets  for building are here: https://doc.qt.io/qt-6/qmainwindow.html#:~:text=A%20main%20window%20provides%20a,image%20of%20the%20layout%20below.

For my simple note app QWidget should be enough.

### 3.2 GUI implementation

#### 3.2.1 Initialization & Arguments
The application is initialized using ```app = QApplication(sys.argv)```
to do so we need to ```import sys```. This provides access to the interpreter's argument list, which is required by the underlying Qt engine to set up the environment.

While the final application will likely be launched via a desktop icon without manual console input, I keep passing the system arguments list for automated testing and debugging during development.

It is useful to refresh a bit about the main in C++, as Qt6 is a C++ library.
For example, here is a nice short overview: https://www.ibm.com/docs/en/i/7.5.0?topic=functions-main-function

#### 3.2.2 Layout Strategy
- Main Window (QWidget)
- Input Area (QWidget)
- Scroll Area (QScrollArea) with Grid (QGridLayout) and Note Cards (QFrame  or QWidget)

Some Qt separation of concerns: Widgets are the elements that we can see (the buttons, text boxes, and containers), while Layouts are the "glue" that positions them.

So for my App:

- Widget Concept (The Objects):
QWidget: the main window and the individual note cards.
QScrollArea: The specialized "viewing area" that allows the window to scroll when the list of notes gets too long.
QLineEdit / QTextEdit: title and body input areas.

- Layout Concept (The Positioning):
QVBoxLayout: Stacks the "Input Area" directly on top of the "Scroll Area."
QGridLayout: Manages the math of the 5-column grid for the note cards.

#### 3.2.3 Vertical layout

This YouTube tutorial helped me to get started: https://www.youtube.com/watch?v=Cc_zaUbF4LM&list=PLqF6vzpT2rGpNb7jx85qvDH9N337Tar0f&index=25
The author uses QMainWindow() but for layout itself it doesn't matter for now

For my app window I choosed a vertical layout, so that the elements are stacked.

Imports for now: ```QVBoxLayout, QLineEdit, QTextEdit, QPushButton```

Order of work:
- define the layout:
```layout = QVBoxLayout()```
- create widgets and instantiate a specific Widget class
in my case I use QLineEdit, QTextEdit, QPushButton
- add widgets to layout, for example:
```layout.addWidget(<widget_name>)```
It's important that the widgets will appear on the window in same order they are added to layout, not in the order they defined.

Example of a basic window with the title area, note text area and save button is in the vertical_layout.py. Run it ```python vertical_layout.py```

For several files code and for usage of
```if __name__ == "__main__":```
it's important to make sure that QWidget is used after the QApplication instance is constructed, so all widgets definitions which are outside ```if __name__ == "__main__":``` block should be wrapped in a class or a funtion. Please see an example in card_example.py