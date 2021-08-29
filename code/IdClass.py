'''
    IdClass
'''

class IdClass():
    
    def __LIST_STR__(list, name):
        from functools import reduce
        sep = lambda a:             \
                "" if a == "" else  \
                "----\n" + a.__str__() + "\n----\n"
        add_line = (lambda n, l:    \
                n if len(l) == 0    \
                else n + "\n")
        return add_line(name, list) \
                    + reduce(lambda a, b: (sep(a)) + sep(b), list, "")

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
    i0 = IdClass(0)
    i0.__whitetest__(f"IdClass('id=0, name=0')")