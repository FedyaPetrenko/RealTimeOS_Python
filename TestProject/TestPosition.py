import unittest
from Position import Position
from PositionDAO import PositionDAO

class AR_Test(unittest.TestCase):

    def test_getAll(self):
        dao = PositionDAO()
        positions = dao.getAll()

    def test_load(self):
        pName = 'Mexanik'
        salary = 1234
        duties = 'fix car'
        requirements = 'time'
        dao = PositionDAO()
        position = dao.getEntity({'PositionName':pName, 'Salary':salary, 'Duties': duties, 'Requirements': requirements})
        self.assertEqual(pName, position.positionName)

    def test_save_delete(self):
        pName = 'Mexanik'
        salary = 1234
        duties = 'fix car'
        requirements = 'time'
        dao = PositionDAO()
        position = Position(pName, salary, duties, requirements)
        dao.save(position)
        del position
        position = dao.getEntity({'PositionName':pName, 'Salary':salary, 'Duties': duties, 'Requirements': requirements})
        dao.delete(position)
        self.assertEqual(position.positionName, pName)

if __name__ == '__main__':    
    unittest.main()  