from Crew import Crew
from Plane import Plane
from PlaneType import PlaneType
from Position import Position
from Race import Race
from Ticket import Ticket
from Worker import Worker

class Manager(object):
    def __init__(self):
        super(Manager, self).__init__()
        self._crew = Crew()
        self._plane = Plane()
        self._planeType = PlaneType()
        self._position = Position()
        self._race = Race()
        self._ticket = Ticket()
        self._worker = Worker()

    @property
    def crew(self):
        return self._crew

    @crew.setter
    def crew(self, value):
        self._crew = value

    @crew.deleter
    def crew(self):
        del self._crew

    @property
    def plane(self):
        return self._plane

    @plane.setter
    def plane(self, value):
        self._plane = value

    @plane.deleter
    def plane(self):
        del self._plane

    @property
    def planeType(self):
        return self._planeType

    @planeType.setter
    def planeType(self, value):
        self._planeType = value

    @planeType.deleter
    def planeType(self):
        del self._planeType

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @position.deleter
    def position(self):
        del self._position

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, value):
        self._race = value

    @race.deleter
    def race(self):
        del self._race

    @property
    def ticket(self):
        return self._ticket

    @ticket.setter
    def ticket(self, value):
        self._ticket = value

    @ticket.deleter
    def ticket(self):
        del self._ticket

    @property
    def worker(self):
        return self._worker

    @worker.setter
    def worker(self, value):
        self._worker = value

    @worker.deleter
    def worker(self):
        del self._worker