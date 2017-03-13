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

    @abstractmethod
    def load(self):
        """вибрати об'єкти з БД"""

    @abstractmethod
    def save(self):
        """зберегти або оновити об'єкт в БД"""

    @abstractmethod
    def _update(self):
        """оновити запис"""

    @abstractmethod
    def delete(self):
        """видалити записи про об'єкт з БД"""


