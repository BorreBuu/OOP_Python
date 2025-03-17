class Notebook:
    """ A Notebook stores notes in string format """

    def __init__(self):
        # protected attribute
        self._notes = []

    def add_note(self, note):
        self._notes.append(note)

    def retrieve_note(self, index):
        return self._notes[index]

    def all_notes(self):
        return ",".join(self._notes)

class NotebookPro(Notebook):
    """ A better Notebook with search functionality """
    def __init__(self):
        # This is OK, the constructor is public despite the underscores
        super().__init__()

    # This works, the protected attribute is accessible to the derived class
    def find_notes(self, search_term):
        found = []
        for note in self._notes:
            print(note)
            if search_term in note:
                found.append(note)

        return found
    
if __name__ == "__main__":
    note = Notebook()
    note.add_note("Hi there!")
    print(note.retrieve_note(0))

    nb_pro = NotebookPro()
    nb_pro.add_note("search")
    print(nb_pro.find_notes("search"))