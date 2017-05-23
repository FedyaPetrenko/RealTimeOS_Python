from Plane import Plane
from PlaneDAO import PlaneDAO

class PlaneUOW(object):
    pool = {}
    newMark = 'n'
    cleanMark = 'c'
    dirtyMark = 'd'
    deletedMark = 'de'
    dao = PlaneDAO()

    def registerNew(self, plane):
        self.pool[plane] = self.newMark

    def registerClean(self, plane):
        self.pool[plane] = self.cleanMark

    def registerDirty(self, plane):
        self.pool[plane] = self.dirtyMark

    def registerDeleted(self, plane):
        self.pool = self.deletedMark

    def commit(self):
        for plane in self.pool:
            if self.pool[plane] is self.newMark:
                dao.save(plane)
            elif self.pool[plane] is self.cleanMark:
                pass  # запис "чистий", отже змінювати БД не потрібно
            elif self.pool[plane] is self.dirtyMark:
                dao.update(plane)
            elif self.pool[plane] is self.deletedMark:
                dao.delete(plane)


