import Person

class Worker(Person.Person):  
    def __init__(self):
        super(Worker,self).__init__()
        self._workerId = None
        self._pib = None
        self._age = None
        self._gender = None
        self._address = None
        self._phone = None
        self._passport = None
        self._positionId = None 
        
    @property
    def workerId(self):
        """Ідентифікатор"""
        return self._workerId

    @workerId.setter
    def workerId(self, value):
        self._workerId = value
        return

    @workerId.deleter
    def workerId(self):
        del self._workerId
        return   
    
    @property
    def pib(self):
        """"""
        return self._pib

    @pib.setter
    def pib(self, value):
        self._pib = value
        return

    @pib.deleter
    def pib(self):
        del self._pib
        return

    @property
    def age(self):
        """"""
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        return

    @age.deleter
    def age(self):
        del self._age
        return 
    
    @property
    def gender(self):
        """"""
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
        return

    @gender.deleter
    def gender(self):
        del self._gender
        return
    
    @property
    def address(self):
        """"""
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
        return

    @address.deleter
    def address(self):
        del self._address
        return 
    
    @property
    def phone(self):
        """"""
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
        return

    @phone.deleter
    def phone(self):
        del self._phone
        return 
    
    @property
    def passport(self):
        """"""
        return self._passport

    @passport.setter
    def passport(self, value):
        self._passport = value
        return

    @passport.deleter
    def passport(self):
        del self._passport
        return 

    @property
    def positionId(self):
        """"""
        return self._positionId

    @positionId.setter
    def positionId(self, value):
        self._positionId = value
        return

    @positionId.deleter
    def positionId(self):
        del self._positionId
        return        


