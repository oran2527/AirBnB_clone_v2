#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'should be db')
    @classmethod
    def setUpClass(self):
        """set up for test"""
        self.db = MySQLdb.connect(
            host=getenv("HBNB_MYSQL_HOST"),
            port=3306,
            user=getenv("HBNB_MYSQL_USER"),
            passwd=getenv("HBNB_MYSQL_PWD"),
            db=getenv("HBNB_MYSQL_DB"),
            charset='utf8'
        )
        self.c = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'should be db')
    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        self.c.close()
        self.db.close()

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

if __name__ == "__main__":
    unittest.main()
