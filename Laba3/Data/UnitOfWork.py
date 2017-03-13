import sqlite3

class UnitOfWork(object):
    db_name = '~/Data/AirportDataBase.db'
    table_DML = 'CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, surname TEXT);'

    def createDB():
        connection = sqlite3.connect(db_name)
        connection.execute(table_DML)
        connection.commit()
        connection.close()

#pool = {}

#newMark = 'n'

#cleanMark = 'c'

#dirtyMark = 'd'

#deletedMark = 'de'

#def registerNew(self, user):

#self.pool[user] = self.newMark

#def registerClean(self, user):

#self.pool[user] = self.cleanMark

#def registerDirty(self, user):

#self.pool[user] = self.dirtyMark

#def registerDeleted(self, user):

#self.pool = self.deletedMark

#def commit(self):

#for user_entry in self.pool:

#if self.pool[user_entry] is self.newMark:

#user_entry.save()

#elif self.pool[user_entry] is self.cleanMark:

#pass # запис "чистий", отже змінювати БД не потрібно

#elif self.pool[user_entry] is self.dirtyMark:

#user_entry.update()

#elif self.pool[user_entry] is self.deletedMark:

#user_entry.delete()


    


