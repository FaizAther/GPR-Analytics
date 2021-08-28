from IdClass import IdClass
'''
    User class
'''

class User(IdClass):
    
    def __init__(self, id):
        super().__init__(id)

    def get_username(self):
        return self.get_name()

    def set_username(self, username):
        self.set_name(username)

    def __repr__(self):
        return f"User('{self.__str__()}')"

    def __str__(self):
        return super().__str__()

    def __whitetest__(self, results):
        print(self.__repr__())
        assert(self.__repr__() == results[0])
        self.set_name("john")
        print(self.__repr__())
        assert(self.__repr__() == results[1])
        assert(self.get_html() == results[2])

if __name__ == "__main__":
    u0 = User(0)
    u0.__whitetest__([
        f"User('id=0, name=0')",
        f"User('id=0, name=john')",
        ""
    ])