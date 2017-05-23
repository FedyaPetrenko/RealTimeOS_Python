from Race import Race
from RaceDAO import RaceDAO

class RaceUOW(object):
    pool = {}
    newMark = 'n'
    cleanMark = 'c'
    dirtyMark = 'd'
    deletedMark = 'de'
    dao = RaceDAO()

    def registerNew(self, race):
        self.pool[race] = self.newMark

    def registerClean(self, race):
        self.pool[race] = self.cleanMark

    def registerDirty(self, race):
        self.pool[race] = self.dirtyMark

    def registerDeleted(self, race):
        self.pool = self.deletedMark

    def commit(self):        
        for race in self.pool:
            if self.pool[race] is self.newMark:                
                dao.save(race)
            elif self.pool[race] is self.cleanMark:
                pass  # запис "чистий", отже змінювати БД не потрібно
            elif self.pool[race] is self.dirtyMark:
                dao.update(race)
            elif self.pool[race] is self.deletedMark:
                dao.delete(race)


