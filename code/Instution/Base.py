'''
    Base Class
'''

class Base():
    
    def __LIST_STR__(list, name):
        sep = lambda e: "\n----\n" + e.__str__() + "\n----\n"
        fold = lambda f, z, l: z if l == [] else f(l[0]) + fold(f, z, l[1:])
        return name + fold(sep, "", list)

    def __init__(self, id):
        self._id            = id
        self._name          = str(id)
        self._description   = ""
        self._html          = ""

    def get_description(self):
        return self._description
    
    def set_description(self, description):
        self._description = description

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def get_html(self):
        return self._html

    def set_html(self, html):
        self._html = html

    def __repr__(self):
        return f"IdClass('{self.__str__()}')"

    def __str__(self):
        return f"id={self.get_id()}, name={self.get_name()}"
    
    def __whitetest__(self, result):
        print(self.__repr__())
        assert(self.__repr__() == result)
        assert(self.get_html() == "")

if __name__ == "__main__":
    i0 = Base(0)
    i0.__whitetest__(f"IdClass('id=0, name=0')")