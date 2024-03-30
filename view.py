from datetime import datetime

navi_button = ['list', 'add', 'show', 'edit', 'delete', 'exit', 'save', 'open']


def input_choice():
    keyword = input('Enter command: ')
    for data in navi_button:
        if keyword == data:
            return keyword
    else:
        print('Enter correct command!')


def print_notes(notes: list[dict[str, str]]):
    if notes:
        print('-' * 130)
        for id, data in enumerate(notes, 1):
            print(f'{id:<3} | {data["title"]:<30} | {data["note"]:<60} | {data["date"]:<20}')
        print('-' * 130)
    else:
        print_message('Something went wrong or notes is empty!')


def print_message(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))


def input_notes(new_id: int):
    temp_note = {}
    print('Enter new note: ')
    temp_note['id'] = str(new_id)
    temp_note['date'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    temp_note['title'] = input('Enter title: ')
    temp_note['note'] = input('Enter notes: ')
    return temp_note


def input_search(message) -> str:
    return input(message)


def input_index(message: str, notes: list) -> int:
    print_notes(notes)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(notes) + 1:
            return int(index)
