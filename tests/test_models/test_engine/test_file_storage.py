#!/usr/bin/python3
""" Defines a class TestFileStorage for FileStorage module. """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Defines tests for FileStorage Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.file_storage1 = FileStorage()

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.file_storage1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.engine.file_storage.FileStorage'>"
        self.assertEqual(str(type(self.file_storage1)), result)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.file_storage1, FileStorage)
        self.assertEqual(type(self.file_storage1), FileStorage)

    def test_functions(self):
        """Test if FileStorage module is documented.
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_save(self):
        """Test if save method is working correctly.
        """
        with open(storage.get_filepath(), 'r', encoding='utf-8') as myFile:
            dump = myFile.read()
        self.assertNotEqual(len(dump), 0)
        temp_d = eval(dump)
        key = self.temp_objs[0].__class__.__name__ + '.'
        key += str(self.temp_objs[0].id)
        self.assertNotEqual(len(temp_d[key]), 0)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(temp_d[key2], KeyError)
        except Exception:
            pass

    def test_reload(self):
        """Tests if reload method is working correctly.
        """
        storage.reload()
        obj_d = storage.all()
        key = self.temp_objs[1].__class__.__name__ + '.'
        key += str(self.temp_objs[1].id)
        self.assertNotEqual(obj_d[key], None)
        self.assertEqual(obj_d[key].id, self.temp_objs[1].id)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except Exception:
            pass

    def test_delete_basic(self):
        """Tests if delete method is working correctly.
        """
        self.assertEqual(storage.delete(BaseModel()), True)
        self.assertEqual(storage.delete(self.temp_objs[2]), True)
        obj_d = storage.all()
        key2 = self.temp_objs[2].__class__.__name__ + '.'
        key2 += str(self.temp_objs[2].id)
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
