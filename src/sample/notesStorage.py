class NotesStorage():
    def add(self, note):
        pass

    def clear():
        pass

    def getAllNotesOf(self, name):
        pass

class NotesService():
    def __init__(self):
        self.store = NotesStorage()

    def add(self, note):
        return self.store.add(note)

    def averageOf(self, name):
        sum = 0
        n = 0

        for i in self.store.getAllNotesOf(name):
            sum += i.note
            n += 1

        return round(sum/n, 2)

    def clear(self):
        return self.store.clear()