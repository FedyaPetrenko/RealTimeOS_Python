import BaseDAO
import sqlite3
from Ticket import Ticket

class TicketDAO(BaseDAO.BaseDAO):
    def __init__(self):
        super(TicketDAO,self).__init__()

    _dbname = 'AirportDataBase.db'

    def getAll(self):
        tickets = []
        query = 'SELECT TicketId, PIB, Passport, Place, RaceId, Price ' \
                'FROM Ticket'
        connection = sqlite3.connect(self._dbname)
        result = connection.execute(query).fetchall()
        for ticket in result:
            ticket = Ticket()
            ticket.ticketId = user_data[0]
            ticket.pib = user_data[1]
            ticket.passport = user_data[2]
            ticket.place = user_data[3]
            ticket.raceId = user_data[4]
            ticket.price = user_data[5]
            tickets.append(ticket)
        connection.close()
        return tickets

    def getEntity(self, paramDict):
        res_ticket = Ticket()
        query = 'SELECT TicketId, PIB, Passport, Place, RaceId, Price ' \
                'FROM Ticket ' \
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
        res_ticket.ticketId = result[0]
        res_ticket.pib = result[1]
        res_ticket.passport = result[2]
        res_ticket.place = result[3]
        res_ticket.raceId = result[4]
        res_ticket.price = result[5]
        return res_ticket

    def save(self, ticket):
        if ticket.ticketId is None:
            query = 'INSERT INTO Ticket ' \
                    '(`PIB`,`Passport`,`Place`,`RaceId`,`Price`) ' \
                    'VALUES ' \
                    '("{pib}", "{passport}", "{place}", "{raceId}", "{price}");'
            filled_query = query.format(pib = ticket.pib,
                                    passport = ticket.passport,
                                    place = ticket.place,
                                    raceId = ticket.raceId,
                                    price = ticket.price)
            connection = sqlite3.connect(self._dbname)
            result = connection.execute(filled_query)
            connection.commit()
            connection.close()
        else:
            self._update(ticket)

    def update(self, ticket):
        query = 'UPDATE Ticket ' \
                'SET '\
                'PIB = "{pib}", ' \
                'Passport = "{passport}", ' \
                'Place = "{place}", ' \
                'RaceId = "{raceId}", ' \
                'Price = "{price}", ' \
                'WHERE TicketId = ?;'
        filled_query = query.format(pib = ticket.pib,
                                    passport = ticket.passport,
                                    place = ticket.place,
                                    raceId = ticket.raceId,
                                    price = ticket.price)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query, ticket.raceId)
        connection.commit()
        connection.close()

    def delete(self, ticket):
        query = 'DELETE FROM Ticket ' \
                'WHERE TicketId = "{ticketId}";'
        filled_query = query.format(ticketId = ticket.ticketId)
        connection = sqlite3.connect(self._dbname)
        connection.execute(filled_query)
        connection.commit()
        return


