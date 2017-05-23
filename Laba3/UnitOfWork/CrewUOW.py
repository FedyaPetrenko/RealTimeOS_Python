from Crew import Crew
from CrewDAO import CrewDAO

class CrewUOW(object):
    pool = {}
    newMark = 'n'
    cleanMark = 'c'
    dirtyMark = 'd'
    deletedMark = 'de'
    dao = CrewDAO()

    def registerNew(self, crew):
        self.pool[crew] = self.newMark

    def registerClean(self, crew):
        self.pool[crew] = self.cleanMark

    def registerDirty(self, crew):
        self.pool[crew] = self.dirtyMark

    def registerDeleted(self, crew):
        self.pool = self.deletedMark

    def commit(self):        
        for crew in self.pool:
            if self.pool[crew] is self.newMark:                
                dao.save(crew)
            elif self.pool[crew] is self.cleanMark:
                pass  # запис "чистий", отже змінювати БД не потрібно
            elif self.pool[crew] is self.dirtyMark:
                dao.update(crew)
            elif self.pool[crew] is self.deletedMark:
                dao.delete(crew)


