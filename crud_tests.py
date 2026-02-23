import db


def run_tests():
    db.init_db()

    db.add_note("note 1", "this is a first note.")
    db.add_note("note 2", "It was a good day.")
    db.add_note("note 3", "I like to play basketball.")

    notes = db.get_notes()
    print("All notes:")
    print(notes)

    print("\nSecond note:")
    print(db.get_note_by_id(2))

    print("\n----------------------------")
    print("------ UPDATE TEST ---------")
    db.update_note(3, "evening note", "I am going to sleep")

    print("Updated note:")
    print(db.get_note_by_id(3))

    print("\n----------------------------")
    print("------ DELETE TEST ---------")
    print("All notes before deletion:")
    print(db.get_notes())

    db.delete_note(2)

    print("All notes after deletion:")
    print(db.get_notes())


if __name__ == "__main__":
    run_tests()