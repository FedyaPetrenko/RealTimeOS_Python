import Transport

class Plane(Transport.Transport):
    def __init__(self):
        super(Plane,self).__init__()
        self._make = None
        self._capacity = None
        self._tonnage = None
        self._dateRelease = None
        self._dateLastFix = None
        
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


