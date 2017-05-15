from abc import ABCMeta, abstractmethod, abstractproperty

class Transport(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def make(self):
        """марка/виробник"""   

    @abstractproperty
    def capacity(self):
        """місткіть"""   

    @abstractproperty
    def tonnage(self):
        """вага"""

    @abstractproperty
    def dateRelease(self):
        """дата виробництва"""

    @abstractproperty
    def dateLastFix(self):
        """дата останнього ремонту"""  


