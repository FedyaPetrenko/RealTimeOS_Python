from Position import Position
from PositionDAO import PositionDAO

class PositionUOW(object):
    pool = {}
    newMark = 'n'
    cleanMark = 'c'
    dirtyMark = 'd'
    deletedMark = 'de'
    dao = PositionDAO()

    def registerNew(self, position):
        self.pool[position] = self.newMark

    def registerClean(self, position):
        self.pool[position] = self.cleanMark

    def registerDirty(self, position):
        self.pool[position] = self.dirtyMark

    def registerDeleted(self, position):
        self.pool = self.deletedMark

    def commit(self):
        for position in self.pool:
            if self.pool[position] is self.newMark:
                dao.save(position)
            elif self.pool[position] is self.cleanMark:
                pass  # запис "чистий", отже змінювати БД не потрібно
            elif self.pool[position] is self.dirtyMark:
                dao.update(position)
            elif self.pool[position] is self.deletedMark:
                dao.delete(position)



