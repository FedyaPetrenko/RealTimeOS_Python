from abc import ABCMeta, abstractmethod, abstractproperty

class Person(object):
    __metaclass__ = ABCMeta

    @abstractproperty   
    def pib(self):
        """піб"""
                   
    @abstractproperty
    def age(self):
        """вік"""

    @abstractproperty
    def gender(self):
        """стать"""

    @abstractproperty
    def adress(self):
        """адреса"""

    @abstractproperty
    def phone(self):
        """номер телефону"""

    @abstractproperty
    def passport(self):
        """серія і номер паспорта"""

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


