class Race(object): 
     def __init__(self):
        self._raceId = None
        self._date = None
        self._time = None
        self._fromPlace = None
        self._toPlace = None  
        self._crewId = None  
        self._planeId = None    

     @property
     def raceId(self):
         """"""
         return self._raceId

     @raceId.setter
     def raceId(self, value):
         self._raceId = value
         return

     @raceId.deleter
     def raceId(self):
         del self._raceId
         return

     @property
     def date(self):
         """"""
         return self._date

     @date.setter
     def date(self, value):
         self._date = value
         return

     @date.deleter
     def date(self):
         del self._date
         return

     @property
     def time(self):
         """"""
         return self._time

     @time.setter
     def time(self, value):
         self._time = value
         return

     @time.deleter
     def time(self):
         del self._time
         return

     @property
     def fromPlace(self):
         """"""
         return self._fromPlace

     @fromPlace.setter
     def fromPlace(self, value):
         self._fromPlace = value
         return

     @fromPlace.deleter
     def fromPlace(self):
         del self._fromPlace
         return

     @property
     def toPlace(self):
         """"""
         return self._toPlace

     @toPlace.setter
     def toPlace(self, value):
         self._toPlace = value
         return

     @toPlace.deleter
     def toPlace(self):
         del self._toPlace
         return

     @property
     def crewId(self):
         """"""
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
     def planeId(self):
         """"""
         return self._planeId

     @planeId.setter
     def planeId(self, value):
         self._planeId = value
         return

     @planeId.deleter
     def planeId(self):
         del self._planeId
         return


