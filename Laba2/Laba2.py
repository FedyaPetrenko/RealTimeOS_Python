import sqlite3

con = sqlite3.connect('AirportDataBase.db')
cur = con.cursor()
cur.execute('''CREATE TABLE Workers(
            WorkerId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            PIB VARCHAR(30),
            Age INTEGER,
            Gender VARCHAR(3),
            Adress VARCHAR(30),
            Phone INTEGER,
            Passport VARCHAR(20),
            PositionId INTEGER ,
            FOREIGN KEY(PositionId) REFERENCES Position(PositionId)
            )''')
cur.execute('''INSERT INTO Workers( WorkerId,PIB,Age,Gender,Adress,Phone,Passport, PositionId) VALUES (1,"Petja",23,"M","kiev",37238,"KV348643", 1)
              ''')
cur.execute('''INSERT INTO Workers( WorkerId,PIB,Age,Gender,Adress,Phone,Passport, PositionId) VALUES (2,"Vasia",43,"M","Lviv",2346508,"KV345643", 1)
''')
cur.execute('''INSERT INTO Workers( WorkerId,PIB,Age,Gender,Adress,Phone,Passport, PositionId) VALUES (3,"Kolia",33,"M","Dnipro",337433,"KV323443",2)
''')
cur.execute('''INSERT INTO Workers( WorkerId,PIB,Age,Gender,Adress,Phone,Passport, PositionId) VALUES (4,"Artem",37,"M","Kiev",837833,"KV32833", 3)
''')

cur.execute('''CREATE TABLE Position(
            PositionId INTEGER PRIMARY KEY AUTOINCREMENT,
            PositionName VARCHAR(30),
            Salary INTEGER,
            Duties VARCHAR(100),
            Requirements VARCHAR(100)
            )''')
cur.execute('''INSERT INTO Position( PositionId,PositionName,Salary,Duties,Requirements) VALUES (1,"Vodii",4000,"drive","time")
''')
cur.execute('''INSERT INTO Position( PositionId,PositionName,Salary,Duties,Requirements) VALUES (2,"Mexanik",5000,"fix car","education")
''')
cur.execute('''INSERT INTO Position( PositionId,PositionName,Salary,Duties,Requirements) VALUES (3,"Vodii",5000,"drive","time")
''')

cur.execute('''CREATE TABLE Plane(
            PlaneId INTEGER PRIMARY KEY AUTOINCREMENT,
            Make VARCHAR(30),
            Capacity INTEGER,
            Tonnage INTEGER,
            TypeId INTEGER,
            TTX VARCHAR(100),
            DateRelease VARCHAR(100),
            DateLastFix VARCHAR(100),
            DateLastFlight VARCHAR(100),
            Hours INTEGER,
            WorkerId INTEGER,
            FOREIGN KEY(WorkerId) REFERENCES Workers(WorkerId),
            FOREIGN KEY(TypeId) REFERENCES PlaneType(PlaneTypeId))
            ''')
cur.execute('''INSERT INTO Plane( PlaneId,Make,Capacity,Tonnage,TTX, DateRelease, DateLastFlight, DateLastFix, Hours, WorkerId, TypeId) VALUES (1,"Boenig",600, 500, "TTX 1", "1995", "2016", "2016", 150, 1, 1)
''')                                                                                                          
cur.execute('''INSERT INTO Plane( PlaneId,Make,Capacity,Tonnage,TTX, DateRelease, DateLastFlight, DateLastFix, Hours, WorkerId, TypeId) VALUES (2,"Boenig",400, 700, "TTX 2", "1996", "2015", "2016", 1150, 2, 1)
''')                                                                                                          
cur.execute('''INSERT INTO Plane( PlaneId,Make,Capacity,Tonnage,TTX, DateRelease, DateLastFlight, DateLastFix, Hours, WorkerId, TypeId) VALUES (3,"Airbus",400, 200, "TTX 3", "1997", "2014", "2016", 2150, 3, 2)
''')

cur.execute('''CREATE TABLE `Crew` (
	`CrewId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Worker1`	INTEGER,
	`Worker2`	INTEGER,
	`Worker3`	INTEGER
);          
            ''')
cur.execute('''INSERT INTO `Crew`(`Worker1`,`Worker2`,`Worker3`) VALUES (1,2,3)
''')



cur.execute('''CREATE TABLE PlaneType(
            PlaneTypeId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(30),
            Assignment VARCHAR(30),
            Restriction VARCHAR(30)
            )''')
cur.execute('''INSERT INTO PlaneType(PlaneTypeId, Name, Assignment, Restriction) VALUES (1,"passPlane","For passengers","Should have wings")
''')
cur.execute('''INSERT INTO PlaneType(PlaneTypeId, Name, Assignment, Restriction) VALUES (2,"anotherPassPlane","For another passengers","Should have wings")
''')


cur.execute('''CREATE TABLE Race(
            RaceId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Date VARCHAR(30),
            Time VARCHAR(30),
            FromPlace VARCHAR(30),
            ToPlace VARCHAR(30),
            CrewId INTEGER,
            PlaneId INTEGER,
            FOREIGN KEY(CrewId) REFERENCES Crew(CrewId),
            FOREIGN KEY(PlaneId) REFERENCES Plane(PlaneId))''')
cur.execute('''INSERT INTO Race( Date,Time,FromPlace,ToPlace,CrewId,PlaneId) VALUES ("11.03.2017","16:42","IEV","DXB",1,1)''')

cur.execute('''CREATE TABLE Ticket(
            TicketId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            PIB VARCHAR(100),
            Passport VARCHAR(100),
            Place INTEGER,
            RaceId INTEGER,
            Price INTEGER,
            FOREIGN KEY(RaceId) REFERENCES Race(RaceId)
            )''')
cur.execute('''INSERT INTO Ticket( PIB,Passport,Place,RaceId,Price) VALUES ("Ivanov Ivan Petrovich","HD111000",65,54,73)
''')
con.commit()
