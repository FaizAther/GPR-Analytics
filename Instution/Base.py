from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

'''
    Base Class
'''
class Base(ABC):

    __DO_SOMETHING__ = lambda f, x: f(x)

    ADD_THING_TO = lambda s, to: list.append(to, s)

    @staticmethod
    def dict_find(s, to):
        sid = s
        if (type(s) == str):
            try:
                sid = int(s)
            except:
                sid = None
        if sid == None and type(s) != int:
            try:
                sid = s.get_id()
            except:
                sid = None
        return to.get(sid) if sid != None else None

    @staticmethod
    def dict_insert(s, to) -> None:
        if (Base.dict_find(s, to) == None):
            to[s.get_id()] = s

    @staticmethod
    def __DO_SOMETHINGS__(f, elems) -> None:
        for e in elems:
            Base.__DO_SOMETHING__(f, e)

    @staticmethod
    def ADD_THINGS_TO(somethings: List[object], to: List[object]) -> None:
        Base.__DO_SOMETHINGS__(lambda x: to.append(x), somethings)

    FOLDL = lambda f, z, l:     \
                z if l == []    \
                else Base.FOLDL(f, (f(z, l[0])), l[1:])

    SEP_OP  = lambda e1, e2: e1 + Base.SEP(e2)
    SEP     = lambda e: "\n----\n" + e.__str__() + "\n----\n"

    @staticmethod
    def __LIST_STR__(values: List, name: str) -> str:
        return name + Base.FOLDL(Base.SEP_OP, "", values)

    def __init__(self, id: int, name: str=None, description: str=None, html=None):
        self._id:           int = id
        self._name:         str = str(id)
        self._description:  str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        self._html:         str = "N.A."
        self.set_name(name)
        self.set_description(description)
        self.set_html(html)

    def get_description(self) -> str:
        return self._description

    def set_description(self, description) -> None:
        if description != None:
            self._description = description

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        if name != None:
            self._name = name

    def get_html(self) -> str:
        return self._html

    def set_html(self, html: str) -> None:
        if html != None:
            self._html = html

    @abstractmethod
    def insert(self) -> str:
        return None

    @abstractmethod
    def generate_html(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}('{self.__repr__()}')"

    @abstractmethod
    def __repr__(self) -> str:
        return f"id={self.get_id()}, name={self.get_name()}"

    DEFAULT_TEST = []

    @abstractmethod
    def __whitetest__(self, result=DEFAULT_TEST) -> bool:
        return True
