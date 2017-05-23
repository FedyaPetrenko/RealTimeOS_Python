import sqlite3

class UnitOfWorkMain(object):
    db_name = '~/Data/AirportDataBase.db'
    workers_table_DML = 'CREATE TABLE Workers(' \
                'WorkerId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' \
                'PIB VARCHAR(30),' \
                'Age INTEGER,' \
                'Gender VARCHAR(3),' \
                'Adress VARCHAR(30),' \
                'Phone INTEGER,' \
                'Passport VARCHAR(20),'\
                'PositionId INTEGER ,' \
                'FOREIGN KEY(PositionId) REFERENCES Position(PositionId)' \
                ' );'

    def createDB():
        connection = sqlite3.connect(db_name)
        connection.execute(workers_table_DML)
        connection.commit()
        connection.close()  
    


