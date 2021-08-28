from IdClass import IdClass

'''
	University class
'''
class University(IdClass):

    def __init__(self, id):
        super().__init__(id)
        self._faculties = []
    
    def get_faculties(self):
        return self._faculties
    
    def add_faculty(self, faculty):
        self._faculties.append(faculty)

    def add_faculties(self, faculties):
        for faculty in faculties:
            self.add_faculty(faculty)
    
    def __repr__(self):
        return f"University('{self.__str__()}')"

    def __str__(self):
        faculties_str = ", faculties="
        if len(self.get_faculties()) > 0:
            faculties_str += "\n"
            for faculty in self.get_faculties():
                faculties_str += "----\n"
                faculties_str += (faculty.__str__())
                faculties_str += ("\n----\n")
        return super().__str__() + faculties_str
    
    def __whitetest__(self, result):
        print(self.__repr__())
        assert(self.__repr__() == result[0])
        self.set_name("john")
        assert(self.__repr__() == result[1])
        self.add_faculty("smith")
        print(self.__repr__())
        assert(self.__repr__() == result[2])
        assert(self.get_html() == result[3])
    
if __name__ == "__main__":
    uni0 = University(0)
    uni0.__whitetest__(result=[
        "University('id=0, name=0, faculties=')",
        "University('id=0, name=john, faculties=')",
        f"University('id=0, name=john, faculties=\n----\nsmith\n----\n')",
        ""
    ])