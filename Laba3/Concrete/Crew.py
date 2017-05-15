from Worker import Worker

class Crew(object):
    def __init__(self):
        self._crewId = None
        self._worker1 = Worker()
        self._worker2 = Worker()
        self._worker3 = Worker()           
        
    @property
    def crewId(self):
        """Crew Id - ідентифікатор екіпажу"""
        return self._crewId

    @crewId.setter
    def crewId(self, value):
        self._crewId = value
        return

    @crewId.deleter
    def crewId(self):
        del self._crewId
        return

    @property
    def worker1(self):
        """worker1 - ідентифікатор першого працівника"""
        return self._worker1

    @worker1.setter
    def worker1(self, value):
        self._worker1 = value
        return

    @worker1.deleter
    def worker1(self):
        del self._worker1
        return

    @property
    def worker2(self):
        """worker2 - ідентифікатор другого працівника"""
        return self._worker2

    @worker2.setter
    def worker2(self, value):
        self._worker2 = value
        return

    @worker2.deleter
    def worker2(self):
        del self._worker2
        return

    @property
    def worker3(self):
        """worker3 - ідентифікатор третього працівника"""
        return self._worker3

    @worker3.setter
    def worker3(self, value):
        self._worke3 = value
        return

    @worker3.deleter
    def worker3(self):
        del self._worker3
        return


