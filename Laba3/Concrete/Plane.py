import Transport

class Plane(Transport.Transport):
    def __init__(self):
        super(Plane,self).__init__()
        self._planeId = None
        self._make = None
        self._capacity = None
        self._tonnage = None
        self._typeId = None
        self._ttx = None
        self._dateRelease = None
        self._dateLastFix = None
        self._dateLastFlight = None
        self._hours = None
        self._workerId = None

    @property
    def planeId(self):
        """Ідентифікатор"""
        return self._planeId

    @planeId.setter
    def planeId(self, value):
        self._planeId = value
        return

    @planeId.deleter
    def planeId(self):
        del self._planeId
        return
        
    @property
    def make(self):
        """марка/виробник"""
        return self._make

    @make.setter
    def make(self, value):
        self._make = value
        return

    @make.deleter
    def make(self):
        del self._make
        return

    @property
    def capacity(self):
        """місткіть"""
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value
        return

    @capacity.deleter
    def capacity(self):
        del self._capacity
        return

    @property
    def tonnage(self):
        """вага"""
        return self._tonnage

    @tonnage.setter
    def tonnage(self, value):
        self._tonnage = value
        return

    @tonnage.deleter
    def tonnage(self):
        del self._tonnage
        return

    @property
    def typeId(self):
        """Ідентифікатор типу"""
        return self._typeId

    @typeId.setter
    def typeId(self, value):
        self._typeId = value
        return

    @typeId.deleter
    def typeId(self):
        del self._typeId
        return

    @property
    def ttx(self):
        """TTX"""
        return self._ttx

    @ttx.setter
    def ttx(self, value):
        self._ttx = value
        return

    @ttx.deleter
    def ttx(self):
        del self._ttx
        return

    @property
    def dateRelease(self):
        """дата останнього ремонту"""
        return self._dateRelease

    @dateRelease.setter
    def dateRelease(self, value):
        self._dateRelease = value
        return

    @dateRelease.deleter
    def dateRelease(self):
        del self._dateRelease
        return

    @property
    def dateLastFix(self):
        """дата останнього ремонту"""
        return self._dateLastFix

    @dateLastFix.setter
    def dateLastFix(self, value):
        self._dateLastFix = value
        return

    @dateLastFix.deleter
    def dateLastFix(self):
        del self._dateLastFix
        return 
    
    @property
    def dateLastFlight(self):
        """дата останнього польоту"""
        return self._dateLastFlight

    @dateLastFlight.setter
    def dateLastFlight(self, value):
        self._dateLastFlight = value
        return

    @dateLastFlight.deleter
    def dateLastFlight(self):
        del self._dateLastFlight
        return    
    
    @property
    def hours(self):
        """сумарна кількість годин польоту"""
        return self._hours

    @hours.setter
    def hours(self, value):
        self._hours = value
        return

    @hours.deleter
    def hours(self):
        del self._hours
        return   
    
    @property
    def workerId(self):
        """ідентифікатор працівника"""
        return self._workerId

    @workerId.setter
    def workerId(self, value):
        self._workerId = value
        return

    @workerId.deleter
    def workerId(self):
        del self._workerId
        return      


