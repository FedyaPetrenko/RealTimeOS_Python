import BaseDAO
import sqlite3
from Crew import Crew

class CrewDAO(BaseDAO.BaseDAO):
    def __init__(self):
        super(CrewDAO,self).__init__()

    _dbname = 'AirportDataBase.db'

    def getAll(self):
        crews = []
        query = 'SELECT CrewId, Worker1, Worker2, Worker3 ' \
                'FROM Crew'
        connection = sqlite3.connect(self._dbname)
        result = connection.execute(query).fetchall()
        for crew in result:
            crew = Crew()
            crew.crewId = user_data[0]
            crew.worker1 = user_data[1]
            crew.worker2 = user_data[2]
            crew.worker3 = user_data[3]
            crews.append(crew)
        connection.close()
        return crews

    def getEntity(self, paramDict):
        res_crew = Crew()
        query = 'SELECT CrewId, Worker1, Worker2, Worker3 ' \
                'FROM Crew ' \
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
        res_crew.crewId = result[0]
        res_crew.worker1 = result[1]
        res_crew.worker2 = result[2]
        res_crew.worker3 = result[3]
        return res_crew

    def save(self, crew):
        if crew.crewId is None:
            query = 'INSERT INTO Crew ' \
                    '(`Worker1`,`Worker2`,`Worker3`) ' \
                    'VALUES ' \
                    '("{worker1}", "{worker2}", "{worker3}");'
            filled_query = query.format(worker1 = crew.worker1,
                                    worker2 = crew.worker2,
                                    worker3 = crew.worker3)
            connection = sqlite3.connect(self._dbname)
            result = connection.execute(filled_query)
            connection.commit()
            connection.close()
        else:
            self._update(crew)

    def update(self, crew):
        query = 'UPDATE Crew ' \
                'SET '\
                'Worker1 = "{worker1}", ' \
                'Worker2 = "{worker2}", ' \
                'Worker3 = "{worker3}", ' \
                'WHERE CrewId = ?;'
        filled_query = query.format(worker1 = crew.worker1,
                                    worker2 = crew.worker2,
                                    worker3 = crew.worker3,
                                    workerId = crew.workerId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query, crew.crewId)
        connection.commit()
        connection.close()

    def delete(self, crew):
        query = 'DELETE FROM Crew ' \
                'WHERE CrewId = "{crewId}";'
        filled_query = query.format(crewId = crew.crewId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query)
        connection.commit()
        return


