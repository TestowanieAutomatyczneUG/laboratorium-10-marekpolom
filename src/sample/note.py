import re

class Note():
    def __init__(self, name, note):
        try:
            if name == None:
                raise Exception('Name can\'t be None')

            if not re.search('^[^\s]*$', str(name)):
                raise Exception('Name can\'t be empty!')

            self.name = str(name)

        except ValueError:
            raise Exception('Value must be string!')
        
        try:
            if not (float(note) >= 2 and float(note) <= 6):
                raise Exception('Value must be >= 2 and <= 6')
            
            self.note = float(note)

        except ValueError:
            raise Exception('Value must be float')

    def getName(self):
        return self.name

    def getNote(self):
        return self.note