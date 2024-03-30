import json


class Notes:

    def __init__(self, path: str = '') -> None:
        self.notes: list[dict[str, str]] = []
        self.path = path

    def open_note(self):
        try:
            with open(self.path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return -1

    def save_note(self):
        with open(self.path, 'w') as file:
            json.dump(self.notes, file)

    def get_id(self) -> int:
        if self.notes:
            id = max(int(value['id']) for value in self.notes) + 1
        else:
            id = 1
        return id

    def add_note(self, note: dict[str, str]):
        self.notes.append(note)
        return note.get('title')

    def get_notes(self) -> list[dict[str, str]]:
        return self.notes

    def delete_note(self, index: int):
        return self.notes.pop(index-1).get('title')

    def search_notes(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for note in self.notes:
            for field in note.values():
                if word.lower().strip() in field.lower().strip():
                    result.append(note)
                    break
        return result

    def change_notes(self, note: dict[str, str], index: int):
        if len(note['title']) > 0:
            self.notes[index-1]['title'] = note['title']
        if len(note['note']) > 0:
            self.notes[index-1]['note'] = note['note']
        self.notes[index-1]['datetime'] = note['datetime']
