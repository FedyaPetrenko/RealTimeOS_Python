class Position(object):
     def __init__(self):
        self._positionId = None
        self._positionName = None
        self._salary = None
        self._duties = None  
        self._requirements = None  

     @property
     def positionId(self):
         """ідентифікатор розташування"""
         return self._positionId

     @positionId.setter
     def positionId(self, value):
         self._positionId = value
         return

     @positionId.deleter
     def positionId(self):
         del self._positionId
         return

     @property
     def positionName(self):
         """назва розташування"""
         return self._positionName

     @positionName.setter
     def positionName(self, value):
         self._positionName = value
         return

     @positionName.deleter
     def positionName(self):
         del self._positionName
         return

     @property
     def salary(self):
         """"""
         return self._salary

     @salary.setter
     def salary(self, value):
         self._salary = value
         return

     @salary.deleter
     def salary(self):
         del self._salary
         return

     @property
     def duties(self):
         """"""
         return self._duties

     @duties.setter
     def duties(self, value):
         self._duties = value
         return

     @duties.deleter
     def duties(self):
         del self._duties
         return

     @property
     def requirements(self):
         """"""
         return self._requirements

     @requirements.setter
     def requirements(self, value):
         self._requirements = value
         return

     @requirements.deleter
     def requirements(self):
         del self._requirements
         return


