import BaseDAO
import sqlite3
from Position import Position

class PositionDAO(BaseDAO.BaseDAO):
    def __init__(self):
        super(PositionDAO,self).__init__()

    _dbname = 'AirportDataBase.db'

    def getAll(self):
        positions = []
        query = 'SELECT PositionId, PositionName, Salary, Duties, Requirements ' \
                'FROM Position'
        connection = sqlite3.connect(self._dbname)
        result = connection.execute(query).fetchall()
        for position in result:
            position = Position()
            position.positionId = user_data[0]
            position.positionName = user_data[1]
            position.salary = user_data[2]
            position.duties = user_data[3]
            position.requirements = user_data[4]
            positions.append(position)
        connection.close()
        return positions

    def getEntity(self, paramDict):
        res_position = Position()
        query = 'SELECT PositionId, PositionName, Salary, Duties, Requirements ' \
                'FROM Position ' \
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
        res_position.positionId = result[0]
        res_position.positionName = result[1]
        res_position.salary = result[2]
        res_position.duties = result[3]
        res_position.requirements = result[4]
        return res_position

    def save(self, position):
        if position.positionId is None:
            query = 'INSERT INTO Position ' \
                    '(`PositionName`,`Salary`,`Duties`, `Requirements`) ' \
                    'VALUES ' \
                    '("{name}", "{salary}", "{duties}", "{requirements}");'
            filled_query = query.format(name = position.positionName,
                                    salary = position.salary,
                                    duties = position.duties,
                                    requirements = position.requirements)
            connection = sqlite3.connect(self._dbname)
            result = connection.execute(filled_query)
            connection.commit()
            connection.close()
        else:
            self._update(position)

    def update(self, position):
        query = 'UPDATE Position ' \
                'SET '\
                'PositionName = "{name}", ' \
                'Salary = "{salary}", ' \
                'Duties = "{duties}", ' \
                'Requirements = "{requirements}", ' \
                'WHERE PositionId = ?;'
        filled_query = query.format(name = position.positionName,
                                    salary = position.salary,
                                    duties = position.duties,
                                    requirements = position.requirements)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query, position.positionId)
        connection.commit()
        connection.close()

    def delete(self, position):
        query = 'DELETE FROM Position ' \
                'WHERE PositionId = "{positionId}";'
        filled_query = query.format(positionId = position.positionId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query)
        connection.commit()
        return



