from Base import Base
'''
    User class
'''

class User(Base):
    
    def HASH_HEX_DIGEST(value):
        import hashlib
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def __init__(self, id):
        super().__init__(id)
        self._engagements = []
        self._password = ""
        self.set_password("password")

    def validate_password(self, password):
        return self._password == User.HASH_HEX_DIGEST(password)

    def set_password(self, password):
        self._password = User.HASH_HEX_DIGEST(password)

    def get_engagements(self):
        return self._engagements

    def add_engagement(self, engagement):
        self.get_engagements().append(engagement)

    def add_engagements(self, engagements):
        for e in engagements:
            self.add_engagement(e)

    def __repr__(self):            
        return f"User('{self.__str__()}')"

    def __str__(self):
        engagements_str = Base.__LIST_STR__(
            self.get_engagements(), ", engagements=")    
        return super().__str__() + engagements_str

    def __whitetest__(self, results):
        print(self.__repr__())
        assert(self.__repr__() == results[0])
        self.set_name("john")
        print(self.__repr__())
        assert(self.__repr__() == results[1])
        self.add_engagement("smith")
        print(self.__repr__())
        assert(self.__repr__() == results[2])
        assert(self.get_html() == results[3])
        self.add_engagements(["doe", "jack"])
        print(self.__repr__())
        assert(self.__repr__() == results[4])

if __name__ == "__main__":
    u0 = User(0)
    u0.__whitetest__([
        f"User('id=0, name=0, engagements=')",
        f"User('id=0, name=john, engagements=')",
        f"User('id=0, name=john, engagements=\n----\nsmith\n----\n')",
        "",
        f"User('id=0, name=john, engagements=\n----\nsmith\n----\n\n----\ndoe\n----\n\n----\njack\n----\n')"
    ])
