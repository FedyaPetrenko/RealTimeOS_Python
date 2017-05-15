class Ticket(object):         
    def __init__(self):
        self._ticketId = None
        self._pib = None
        self._passport = None
        self._place = None  
        self._raceId = None  
        self._price = None  

    @property
    def ticketId(self):
        """"""
        return self._ticketId

    @ticketId.setter
    def ticketId(self, value):
        self._ticketId = value
        return

    @ticketId.deleter
    def ticketId(self):
        del self._ticketId
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
    def place(self):
        """"""
        return self._place

    @place.setter
    def place(self, value):
        self._place = value
        return

    @place.deleter
    def place(self):
        del self._place
        return

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
    def price(self):
        """"""
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        return

    @price.deleter
    def price(self):
        del self._price
        return
   
