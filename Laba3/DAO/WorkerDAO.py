import BaseDAO
import sqlite3
from Worker import Worker

class WorkerDAO(BaseDAO.BaseDAO):
    def __init__(self):
        super(WorkerDAO,self).__init__()

    _dbname = 'AirportDataBase.db'

    def getAll(self):
        workers = []
        query = 'SELECT WorkerId, PIB, Age, Gender, Adress, Phone, Passport, PositionId ' \
                'FROM Workers'
        connection = sqlite3.connect(self._dbname)
        result = connection.execute(query).fetchall()
        for worker in result:
            worker = Worker()
            worker.workerId = user_data[0]
            worker.pib = user_data[1]
            worker.age = user_data[2]
            worker.gender = user_data[3]
            worker.address = user_data[4]
            worker.phone = user_data[5]
            worker.passport = user_data[6]
            worker.positionId = user_data[7]
            workers.append(worker)
        connection.close()
        return workers

    def getEntity(self, paramDict):
        res_worker = Worker()
        query = 'SELECT WorkerId, PIB, Age, Gender, Adress, Phone, Passport, PositionId ' \
                'FROM Workers ' \
                'WHERE '
        equal_substr = '{attr_name} = ?'
        counter = len(paramDict)
        args=[]
        for param in paramDict:
            query += equal_substr.format(attr_name=param)
            args.append(paramDict[param])
            if counter == 1:
                query += ';'
            else:
                query += ' AND '
            counter -= 1
        connection = sqlite3.connect(self._dbname)
        result = connection.execute(query,args).fetchone()
        connection.close()       
        res_worker.workerId = result[0]
        res_worker.pib = result[1]
        res_worker.age = result[2]
        res_worker.gender = result[3]
        res_worker.address = result[4]
        res_worker.phone = result[5]
        res_worker.passport = result[6]
        res_worker.positionId = result[7]
        return res_worker

    def save(self, worker):
        if worker.workerId is None:
            query = 'INSERT INTO Workers ' \
                    '(`PIB`,`Age`,`Gender`,`Adress`,`Phone`,`Passport`,`PositionId`) ' \
                    'VALUES ' \
                    '("{pib}", "{age}", "{gender}", "{adress}", "{phone}", "{passport}", "{positionId}");'
            filled_query = query.format(pib = worker.pib,
                                    age = worker.age,
                                    gender = worker.gender,
                                    adress = worker.adress,
                                    phone = worker.phone,
                                    passport = worker.passport,
                                    positionId = worker.positionId)
            connection = sqlite3.connect(self._dbname)
            result = connection.execute(filled_query)
            connection.commit()
            connection.close()
        else:
            self._update(worker)

    def update(self, worker):
        query = 'UPDATE Workers ' \
                'SET '\
                'PIB = "{pib}", ' \
                'Age = "{age}", ' \
                'Gender = "{gender}", ' \
                'Adress = "{adress}", ' \
                'Phone = "{phone}", ' \
                'Passport = "{passport}", ' \
                'PositionId = "{positionId}", ' \
                'WHERE WorkerId = ?;'
        filled_query = query.format(pib = worker.pib,
                                    age = worker.age,
                                    gender = worker.gender,
                                    adress = worker.adress,
                                    phone = worker.phone,
                                    passport = worker.passport,
                                    positionId = worker.positionId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query, worker.workerId)
        connection.commit()
        connection.close()

    def delete(self, worker):
        query = 'DELETE FROM Workers ' \
                'WHERE WorkerId = "{workerId}";'
        filled_query = query.format(workerId = worker.workerId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query)
        connection.commit()
        return




