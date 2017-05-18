import BaseDAO
import sqlite3
from Race import Race

class RaceDAO(BaseDAO.BaseDAO):
    def __init__(self):
        super(RaceDAO,self).__init__()

    _dbname = 'AirportDataBase.db'

    def getAll(self):
        races = []
        query = 'SELECT RaceId, Date, Time, FromPlace, ToPlace, CrewId, PlaneId ' \
                'FROM Race'
        connection = sqlite3.connect(self._dbname)
        result = connection.execute(query).fetchall()
        for race in result:
            race = Race()
            race.raceId = user_data[0]
            race.date = user_data[1]
            race.time = user_data[2]
            race.fromPlace = user_data[3]
            race.toPlace = user_data[4]
            race.crewId = user_data[5]
            race.planeId = user_data[6]
            races.append(race)
        connection.close()
        return races

    def getEntity(self, paramDict):
        res_race = Race()
        query = 'SELECT RaceId, Date, Time, FromPlace, ToPlace, CrewId, PlaneId ' \
                'FROM Race ' \
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
        res_race.raceId = result[0]
        res_race.date = result[1]
        res_race.time = result[2]
        res_race.fromPlace = result[3]
        res_race.toPlace = result[4]
        res_race.crewId = result[5]
        res_race.planeId = result[6]
        return res_race

    def save(self, race):
        if race.raceId is None:
            query = 'INSERT INTO Race ' \
                    '(`Date`,`Time`,`FromPlace`,`ToPlace`,`CrewId`,`PlaneId`) ' \
                    'VALUES ' \
                    '("{date}", "{time}", "{fromPlace}", "{toPlace}", "{crewId}", "{planeId}");'
            filled_query = query.format(date = race.date,
                                    time = race.time,
                                    fromPlace = race.fromPlace,
                                    toPlace = race.toPlace,
                                    crewId = race.crewId,
                                    planeId = race.planeId)
            connection = sqlite3.connect(self._dbname)
            result = connection.execute(filled_query)
            connection.commit()
            connection.close()
        else:
            self._update(race)

    def update(self, race):
        query = 'UPDATE Race ' \
                'SET '\
                'Date = "{date}", ' \
                'Time = "{time}", ' \
                'FromPlace = "{fromPlace}", ' \
                'ToPlace = "{toPlace}", ' \
                'CrewId = "{crewId}", ' \
                'PlaneId = "{planeId}", ' \
                'WHERE RaceId = ?;'
        filled_query = query.format(date = race.date,
                                    time = race.time,
                                    fromPlace = race.fromPlace,
                                    toPlace = race.toPlace,
                                    crewId = race.crewId,
                                    planeId = race.planeId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query, race.raceId)
        connection.commit()
        connection.close()

    def delete(self, race):
        query = 'DELETE FROM Race ' \
                'WHERE RaceId = "{raceId}";'
        filled_query = query.format(raceId = race.raceId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query)
        connection.commit()
        return


