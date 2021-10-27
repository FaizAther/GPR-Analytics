from __future__ import annotations

from typing import TYPE_CHECKING

from abc import abstractmethod
from Instution.Base import Base
from datetime import date, datetime

class Announcement(Base):

    def __init__(self, id, description, time):
        super().__init__(id, description=description)
        self._timestamp = datetime.now() if time == None else time
        self._reoucrces = []

    def get_reources(self):
        return self._reoucrces
    
    def add_resource(self, resource):
        self._reoucrces.append(resource)
    
    def add_resources(self, resources):
        for r in resources:
            self.add_resource(r)

    def get_timestamp(self):
        return self._timestamp

    def set_timestamp(self, timestamp):
        self._timestamp = timestamp

    def __whitetest__(self, result=...) -> bool:
        return super().__whitetest__(result=result)
    
    def __repr__(self) -> str:
        return f"{super().__repr__()}, description={self.get_description()}"
    
    def generate_html(self) -> str:
        return super().generate_html()
    
    def insert(self) -> str:
        return super().insert()

if __name__ == "__main__":
    test_annon = Announcement(0)
    print(test_annon)