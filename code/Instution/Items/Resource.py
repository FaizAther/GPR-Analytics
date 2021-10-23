from __future__ import annotations

from typing import TYPE_CHECKING

from abc import abstractmethod
from Instution.Base import Base

class Resource(Base):

    def __init__(self, id, data=None):
        super().__init__(id)
        self._data = data
    
    def get_data(self):
        return self._data
    
    def set_data(self, data):
        self._data = data

    def __whitetest__(self, result=...) -> bool:
        return super().__whitetest__(result=result)
    
    def __repr__(self) -> str:
        return f"{super().__repr__()}"
    
    def generate_html(self) -> str:
        return super().generate_html()
    
    def insert(self) -> str:
        return super().insert()
    