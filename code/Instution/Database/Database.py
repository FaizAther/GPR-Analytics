from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

import sqlite3

if TYPE_CHECKING:
    from typing import Tuple, List, Dict, Any

class Database:

    def __init__(self):
        self.client = None
        self.bucket = "gpr"
        self.connection()

    @abstractmethod
    def connection(self) -> None:
       pass

    @abstractmethod
    def write(self) -> None:
       pass

    @abstractmethod
    def query(self) -> List[Tuple[Any]]:
       pass

class SqliteDB(Database):
    def __init__(self):
        super().__init__()
 
    def connection(self) -> None:
        """Creates a connection to Sqlite3 DB"""
        self.client = sqlite3.connect(self.bucket + '.db')
        self.cursor = self.client.cursor()

    def base(self, query: str) -> None:
        """ Writes the signal to sqliteDB"""
        self.cursor.execute(query)
        self.client.commit()
    
    def write(self, query) -> None:
        """ Update Operand """
        self.base(query)

    def update(self, query) -> None:
        """ Update Operand """
        self.base(query)

    def delete(self, query) -> None:
        """ Update Operand """
        self.base(query)
    
    def query(self, query: str) -> Dict[str, Any]:
        """ Queries from DB and returns the results of the query """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
"""

class GprDataBase():


connection = sqlite3.connect("gpr.db")
cursor = connection.cursor()

query = "SELECT * FROM User;"
cursor.execute(query)

result = cursor.fetchall()
print(result)

connection.commit()
connection.close()
"""