import  sqlite3

DB_NAME='notes.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor=conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                body TEXT NOT NULL,
                image TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP 
            )
        """)
        conn.commit()

def add_note(title, body, image=None):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO notes(title, body, image) VALUES(?, ?, ?)", (title, body, image)
        )
        conn.commit()

def get_notes():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, timestamp from notes ORDER BY timestamp DESC")
        return cursor.fetchall()
    
def get_note_by_id(note_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes WHERE id=?", (note_id,))
        result = cursor.fetchone()
        return result if result else None #id doesn't exist
    

def update_note(note_id, title, body, image=None):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE notes
            SET title = ?, body = ?, image = ?
            WHERE id = ?
            """,
            (title, body, image, note_id)
        )
        conn.commit()


def delete_note(note_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()