from IdClass import IdClass
from EventType import EventType
from datetime import datetime
'''
    Event Class
'''
class Event(IdClass):
    def __init__(self, id):
        super().__init__(id)
        self._date_duration = {datetime.now : 0}
        self._manager = None
        self._organizers = []
        self._guests = []
        self._invitees = []
        self._attendance = []
        self._locations = []
        self._resources = []
        self._type = EventType.DEFAULT