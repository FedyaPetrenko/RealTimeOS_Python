from PlaneType import PlaneType
from PlaneTypeDAO import PlaneTypeDAO

class PlaneTypeUOW(object):
    pool = {}
    newMark = 'n'
    cleanMark = 'c'
    dirtyMark = 'd'
    deletedMark = 'de'
    dao = PlaneTypeDAO()

    def registerNew(self, planeType):
        self.pool[planeType] = self.newMark

    def registerClean(self, planeType):
        self.pool[planeType] = self.cleanMark

    def registerDirty(self, planeType):
        self.pool[planeType] = self.dirtyMark

    def registerDeleted(self, planeType):
        self.pool = self.deletedMark

    def commit(self):        
        for planeType in self.pool:
            if self.pool[planeType] is self.newMark:                
                dao.save(planeType)
            elif self.pool[planeType] is self.cleanMark:
                pass  # запис "чистий", отже змінювати БД не потрібно
            elif self.pool[planeType] is self.dirtyMark:
                dao.update(planeType)
            elif self.pool[planeType] is self.deletedMark:
                dao.delete(planeType)


