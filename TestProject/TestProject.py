# -*- coding: UTF-8 -*-   
import unittest
from user import User

class AR_Test(unittest.TestCase):

    def test_user_save(self): 
        tuser = User() 
        tuser.name = 'Test'
        tuser.surname = 'User'
        tuser.save()  
         
    def test_user_load_(self): 
        target_name = 'Test'
        target_surname = 'User'
        save_user = User() # додаємо користувача, щоб не залежати від стану БД  
        save_user.name = target_name
        save_user.surname = target_surname
        save_user.save() 
        del save_user
        testuser = User()
        testuser.load({'name':target_name, 'surname':target_surname})
        self.assertEqual(target_name, testuser.name, 'incorrect name loading')
        self.assertEqual(target_surname, testuser.surname, 'incorrect surname loading')
    
    def test_user_update(self):
        target_name = 'Test'
        target_surname = 'User'
        testuser = User()
        testuser.load({'name': target_name, 'surname': target_surname}) 
        testuser.name = 'Deletable'
        testuser.surname = 'Deletable'
        testuser.save()

    def test_user_delete(self):
        target_name = 'Test' 
        target_surname = 'User'
        testuser = User() 
        testuser.load({'name': target_name, 'surname': target_surname})
        testuser.delete()

if __name__ == '__main__': # якщо файл запущено, а не імпортовано, то виконається наступний код
    unittest.main()