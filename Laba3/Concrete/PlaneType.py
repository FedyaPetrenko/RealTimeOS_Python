class PlaneType(object):
     def __init__(self):
        self._crewId = None
        self._name = None
        self._assignment = None
        self._restriction = None  

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
     def name(self):
         """Назва типу"""
         return self._name

     @name.setter
     def name(self, value):
         self._name = value
         return

     @name.deleter
     def name(self):
         del self._name
         return

     @property
     def assignment(self):
         """"""
         return self._assignment

     @assignment.setter
     def assignment(self, value):
         self._assignment = value
         return

     @assignment.deleter
     def assignment(self):
         del self._assignment
         return

     @property
     def restriction(self):
         """"""
         return self._restriction

     @restriction.setter
     def restriction(self, value):
         self._restriction = value
         return

     @restriction.deleter
     def restriction(self):
         del self._restriction
         return


