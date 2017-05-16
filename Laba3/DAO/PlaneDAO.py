import BaseDAO
import sqlite3
from Plane import Plane

class PlaneDAO(BaseDAO.BaseDAO):
    def __init__(self):
        super(PlaneDAO,self).__init__()

    _dbname = 'AirportDataBase.db'

    def getAll(self):
        planes = []
        query = 'SELECT PlaneId, Make, Capacity, Tonnage, TypeId, TTX, DateRelease, DateLastFix, DateLastFlight, Hours, WorkerId ' \
                'FROM Plane'
        connection = sqlite3.connect(self._dbname)
        result = connection.execute(query).fetchall()
        for plane in result:
            plane = Plane()
            plane.planeId = user_data[0]
            plane.make = str(user_data[1])
            plane.capacity = user_data[2]
            plane.tonnage = user_data[3]
            plane.typeId = user_data[4]
            plane.ttx = str(user_data[5])
            plane.dateRelease = user_data[6]
            plane.dateLastFix = user_data[7]
            plane.dateLastFlight = user_data[8]
            plane.hours = user_data[9]
            plane.workerId = user_data[10]
            planes.append(plane)
        connection.close()
        return planes

    def getEntity(self, paramDict):
        res_plane = Plane()
        query = 'SELECT PlaneId, Make, Capacity, Tonnage, TypeId, TTX, DateRelease, DateLastFix, DateLastFlight, Hours, WorkerId ' \
                'FROM Plane ' \
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
        res_plane.planeId = result[0]
        res_plane.make = str(result[1])
        res_plane.capacity = result[2]
        res_plane.tonnage = result[3]
        res_plane.typeId = result[4]
        res_plane.ttx = str(result[5])
        res_plane.dateRelease = result[6]
        res_plane.dateLastFix = result[7]
        res_plane.dateLastFlight = result[8]
        res_plane.hours = result[9]
        res_plane.workerId = result[10]
        return res_plane

    def save(self, plane):
        if plane.planeId is None:
            query = 'INSERT INTO Plane ' \
                    '(Make, Capacity, Tonnage, TypeId, TTX, DateRelease, DateLastFix, DateLastFlight, Hours, WorkerId) ' \
                    'VALUES ' \
                    '("{make}", "{capacity}", "{tonnage}", "{typeId}", "{ttx}", "{dateRelease}", "{dateLastFix}", "{dateLastFlight}", "{hours}", "{workerId}");'
            filled_query = query.format(make = plane.make,
                                    capacity = plane.capacity,
                                    tonnage = plane.tonnage,
                                    typeId = plane.typeId,
                                    ttx = plane.ttx,
                                    dateRelease = plane.dateRelease,
                                    dateLastFix = plane.dateLastFix,
                                    dateLastFlight = plane.dateLastFlight,
                                    hours = plane.hours,
                                    workerId = plane.workerId)
            connection = sqlite3.connect(self._dbname)
            result = connection.execute(filled_query)
            connection.commit()
            connection.close()
        else:
            self._update(plane)

    def update(self, plane):
        query = 'UPDATE Plane ' \
                'SET '\
                'Make = "{make}", ' \
                'Capacity = "{capacity}", ' \
                'Tonnage = "{tonnage}", ' \
                'TypeId = "{typeId}", ' \
                'TTX = "{ttx}", ' \
                'DateRelease = "{dateRelease}", ' \
                'DateLastFix = "{dateLastFix}", ' \
                'DateLastFlight = "{dateLastFlight}", ' \
                'Hours = "{hours}", ' \
                'WorkerId = "{workerId}", ' \
                'WHERE PlaneId = ?;'
        filled_query = query.format(make = plane.make,
                                    capacity = plane.capacity,
                                    tonnage = plane.tonnage,
                                    typeId = plane.typeId,
                                    ttx = plane.ttx,
                                    dateRelease = plane.dateRelease,
                                    dateLastFix = plane.dateLastFix,
                                    dateLastFlight = plane.dateLastFlight,
                                    hours = plane.hours,
                                    workerId = plane.workerId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query, plane.planeId)
        connection.commit()
        connection.close()

    def delete(self, plane):
        query = 'DELETE FROM Plane ' \
                'WHERE PlaneId = "{planeId}";'
        filled_query = query.format(planeId = plane.planeId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query)
        connection.commit()
        return