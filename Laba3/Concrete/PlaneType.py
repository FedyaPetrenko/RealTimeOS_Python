class PlaneType(object):
     def __init__(self):
        self._planeTypeId = None
        self._name = None
        self._assignment = None
        self._restriction = None  

     @property
     def planeTypeId(self):
         """Crew Id - ідентифікатор екіпажу"""
         return self._planeTypeId

     @planeTypeId.setter
     def planeTypeId(self, value):
         self._planeTypeId = value
         return

     @planeTypeId.deleter
     def planeTypeId(self):
         del self._planeTypeId
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


