## Notes App

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

### Creating a DataBase with sqlite3
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


