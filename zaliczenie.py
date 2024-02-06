import json
import os
import datetime
import random

class NoteManager:
    def __init__(self):
        # Initialize the note manager
        self.notes = []  # List to hold notes
        self.load_notes()  # Load existing notes from JSON file

    def load_notes(self):
        # Load existing notes from a JSON file if it exists
        try:
            with open("notes.json", "r") as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            pass  # If file doesn't exist, continue

    def save_notes(self):
        # Save notes to a JSON file
        with open("notes.json", "w") as file:
            json.dump(self.notes, file, indent=2)

    def add_note(self, title, content):
        # Add a new note with a random identifier
        new_note = {
            'id': random.randint(10000, 99999),
            'title': title,
            'content': content,
            'created_at': str(datetime.datetime.now())
        }
        self.notes.append(new_note)  # Add new note to the list
        self.save_notes()  # Save notes after adding a new one

    def edit_note(self, note_id, new_title, new_content):
        # Edit an existing note by its identifier
        for note in self.notes:
            if note['id'] == note_id:
                note['title'] = new_title
                note['content'] = new_content
                note['edited_at'] = str(datetime.datetime.now())
                self.save_notes()  # Save notes after editing
                return True  # Return True if the note was successfully edited
        return False  # Return False if the note with the given id was not found

    def delete_note(self, note_id):
        # Delete a note by its identifier
        self.notes = [note for note in self.notes if note['id'] != note_id]
        self.save_notes()  # Save notes after deleting

    def display_notes(self):
        # Display a list of notes with their titles and identifiers
        if not self.notes:
            print("No notes found.")  # Message if no notes found
            return
        print("\nList of Notes:")
        for note in self.notes:
            title = note['title']
            if 'edited_at' in note:
                title = f"\033[92m{title}\033[0m"  # Green color for edited notes
            print(f"{title} ({note['id']})")
            print(f"  Created at: {note['created_at']}")
            if 'edited_at' in note:
                print(f"  Last edited at: {note['edited_at']}")
            print(f"  Content: {note['content']}\n")

if __name__ == "__main__":
    note_manager = NoteManager()

    while True:
        # Display a simple menu for user interaction
        print("\nChoose operation:")
        print("1. Add note")
        print("2. Edit note")
        print("3. Delete note")
        print("4. Display notes")
        print("5. Exit")

        try:
            operation = int(input("Your choice (1-5): "))
        except ValueError:
            print("Error: Enter a valid number.")
            continue

        if operation == 1:
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            note_manager.add_note(title, content)
            print("Note added successfully.")
        elif operation == 2:
            note_manager.display_notes()
            note_id = int(input("Enter note id to edit: "))
            if note_manager.edit_note(note_id, input("New title: "), input("New content: ")):
                print("Note edited successfully.")
            else:
                print("Error: Note with the given id not found.")
        elif operation == 3:
            note_manager.display_notes()
            note_id = int(input("Enter note id to delete: "))
            note_manager.delete_note(note_id)
            print("Note deleted successfully.")
        elif operation == 4:
            note_manager.display_notes()
        elif operation == 5:
            print("Thank you for using the note management program. Goodbye!")
            break
        else:
            print("Error: Enter a number between 1 and 5.")
