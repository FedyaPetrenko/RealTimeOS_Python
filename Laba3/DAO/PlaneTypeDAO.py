import BaseDAO
import sqlite3
from PlaneType import PlaneType

class PlaneTypeDAO(BaseDAO.BaseDAO):
    def __init__(self):
        super(PlaneTypeDAO,self).__init__()

    _dbname = 'AirportDataBase.db'

    def getAll(self):
        planeTypes = []
        query = 'SELECT PlaneTypeId, Name, Assignment, Restriction ' \
                'FROM PlaneType'
        connection = sqlite3.connect(self._dbname)
        result = connection.execute(query).fetchall()
        for planeType in result:
            planeType = PlaneType()
            planeType.planeTypeId = user_data[0]
            planeType.name = user_data[1]
            planeType.assignment = user_data[2]
            planeType.restriction = user_data[3]
            planeTypes.append(planeType)
        connection.close()
        return planeTypes

    def getEntity(self, paramDict):
        res_planeType = PlaneType()
        query = 'SELECT PlaneTypeId, Name, Assignment, Restriction ' \
                'FROM PlaneType ' \
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
        res_planeType.planeTypeId = result[0]
        res_planeType.name = result[1]
        res_planeType.assignment = result[2]
        res_planeType.restriction = result[3]
        return res_planeType

    def save(self, planeType):
        if planeType.planeTypeId is None:
            query = 'INSERT INTO PlaneType ' \
                    '(Name, Assignment, Restriction) ' \
                    'VALUES ' \
                    '("{name}", "{assignment}", "{restriction}");'
            filled_query = query.format(name = planeType.name,
                                    assignment = planeType.assignment,
                                    restriction = planeType.restriction)
            connection = sqlite3.connect(self._dbname)
            result = connection.execute(filled_query)
            connection.commit()
            connection.close()
        else:
            self._update(planeType)

    def update(self, planeType):
        query = 'UPDATE PlaneType ' \
                'SET '\
                'Name = "{name}", ' \
                'Assignment = "{assignment}", ' \
                'Restriction = "{restriction}", ' \
                'WHERE PlaneTypeId = ?;'
        filled_query = query.format(name = planeType.name,
                                    assignment = planeType.assignment,
                                    restriction = planeType.restriction)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query, planeType.planeTypeId)
        connection.commit()
        connection.close()

    def delete(self, planeType):
        query = 'DELETE FROM PlaneType ' \
                'WHERE PlaneTypeId = "{planeTypeId}";'
        filled_query = query.format(planeTypeId = planeType.planeTypeId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query)
        connection.commit()
        return





