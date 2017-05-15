from abc import ABCMeta, abstractmethod, abstractproperty

class BaseDAO(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getAll(self):
        """отримати всі записи з таблиці"""

    @abstractmethod
    def getEntity(self, id):
        """отримати запис з таблиці по id"""

    @abstractmethod
    def save(self, entity):
        """зберегти новий запис"""

    @abstractmethod
    def update(self, entity):
         """оновити запис у таблиці"""

    @abstractmethod
    def delete(self, entity):
         """оновити запис у таблиці"""