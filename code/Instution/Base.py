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
    
    add_something = lambda s, to: list.append(to, s)

    def __DO_SOMETHINGS__(f, elems):
        for e in elems:
            Base.__DO_SOMETHING__(f, e)

    def add_somethings(somethings: List[object], to: List[object]) -> None:
        Base.__DO_SOMETHINGS__(lambda x: to.append(x), somethings)

    FOLDL = lambda f, z, l:     \
                z if l == []    \
                else Base.FOLDL(f, (f(z, l[0])), l[1:])

    SEP_OP  = lambda e1, e2: e1 + Base.SEP(e2)
    SEP     = lambda e: "\n----\n" + e.__str__() + "\n----\n"

    def __LIST_STR__(values: List, name: str) -> str:
        return name + Base.FOLDL(Base.SEP_OP, "", values)

    def __init__(self, id: int):
        self._id:           int = id
        self._name:         str = str(id)
        self._description:  str = ""
        self._html:         str = ""

    def get_description(self) -> str:
        return self._description

    def set_description(self, description) -> None:
        self._description = description

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> str:
        self._name = name

    def get_html(self) -> str:
        return self._html

    def set_html(self, html: str) -> None:
        self._html = html

    @abstractmethod
    def generate_html(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        return f"Base('{self.__str__()}')"

    @abstractmethod
    def __str__(self) -> str:
        return f"id={self.get_id()}, name={self.get_name()}"
