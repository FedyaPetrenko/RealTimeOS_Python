from Worker import Worker
from WorkerDAO import WorkerDAO

class WorkerUOW(object):
    pool = {}
    newMark = 'n'
    cleanMark = 'c'
    dirtyMark = 'd'
    deletedMark = 'de'
    dao = WorkerDAO()

    def registerNew(self, worker):
        self.pool[worker] = self.newMark

    def registerClean(self, worker):
        self.pool[worker] = self.cleanMark

    def registerDirty(self, worker):
        self.pool[worker] = self.dirtyMark

    def registerDeleted(self, worker):
        self.pool = self.deletedMark

    def commit(self):        
        for worker in self.pool:
            if self.pool[worker] is self.newMark:                
                dao.save(worker)
            elif self.pool[worker] is self.cleanMark:
                pass  # запис "чистий", отже змінювати БД не потрібно
            elif self.pool[worker] is self.dirtyMark:
                dao.update(worker)
            elif self.pool[worker] is self.deletedMark:
                dao.delete(worker)


