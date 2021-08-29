from IdClass import IdClass
'''
    Faculty class
'''
class Faculty(IdClass):
    def __init__(self, id):
        super().__init__(id)
        self._courses = []
        self._locations = []