from Ticket import Ticket
from TicketDAO import TicketDAO

class TicketUOW(object):
    pool = {}
    newMark = 'n'
    cleanMark = 'c'
    dirtyMark = 'd'
    deletedMark = 'de'
    dao = TicketDAO()

    def registerNew(self, ticket):
        self.pool[planticketeType] = self.newMark

    def registerClean(self, ticket):
        self.pool[ticket] = self.cleanMark

    def registerDirty(self, ticket):
        self.pool[ticket] = self.dirtyMark

    def registerDeleted(self, ticket):
        self.pool = self.deletedMark

    def commit(self):        
        for ticket in self.pool:
            if self.pool[ticket] is self.newMark:                
                dao.save(ticket)
            elif self.pool[ticket] is self.cleanMark:
                pass  # запис "чистий", отже змінювати БД не потрібно
            elif self.pool[ticket] is self.dirtyMark:
                dao.update(ticket)
            elif self.pool[ticket] is self.deletedMark:
                dao.delete(ticket)


