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
    def address(self):
        """адреса"""

    @abstractproperty
    def phone(self):
        """номер телефону"""

    @abstractproperty
    def passport(self):
        """серія і номер паспорта"""   


