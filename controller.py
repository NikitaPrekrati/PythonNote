import view
import model

my_notes = model.Notes('notes.json')


def start():

    while True:
        print('Main menu:\n',
              'open - open note\n',
              'list - show all notes\n',
              'add  - add new note\n',
              'show - show note\n',
              'edit - edit note\n',
              'save - save note\n',
              'delete  - delete note\n',
              'exit - exit\n')

        choice = view.input_choice()

        match choice:
            case "open":
                my_notes.open_note()
                view.print_message('Notes successfully open')
            case "save":
                my_notes.save_note()
                view.print_message('Note successfully saved')
            case "list":
                notes = my_notes.get_notes()
                view.print_notes(notes)
                view.print_message('What you gonna do?')
            case "add":
                note = view.input_notes(my_notes.get_id())
                title = my_notes.add_note(note)
                view.print_message('Note "' + title + '" successfully added!')
            case "show":
                word = view.input_search('What you want to find?')
                result = my_notes.search_notes(word)
                view.print_notes(result)
            case "edit":
                notes = my_notes.get_notes()
                index = view.input_index('Enter number of note to show: ', notes)
                note = view.input_notes(my_notes.get_id())
                result = my_notes.change_notes(note, index)
                view.print_message('Note ' + result + ' successfully changed!')
            case "delete":
                notes = my_notes.get_notes()
                index = view.input_index('Enter # of note to delete: ', notes)
                title = my_notes.delete_note(index)
                view.print_message('Note "' + title + '" successfully deleted!')
            case "exit":
                view.print_message('Have a nice day!')
                break
