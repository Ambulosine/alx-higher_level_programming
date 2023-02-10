#!/usr/bin/python3
'''unittest file for square module'''
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest
import json
from os import path as ospath


class TestInstantiation(unittest.TestCase):
    '''tests instantiation of sq objects'''

    def setUp(self):
        self.sq = Square(5, test=True)
        self.sq1 = Square(7, 2, 2, test=True)
        self.sq2 = Square(3, 0, 1, 40, test=True)

    def tearDown(self):
        del self.sq
        del self.sq1
        del self.sq2

    def test_width(self):
        self.assertEqual(self.sq.width, 5)
        self.assertEqual(self.sq1.width, 7)
        self.assertEqual(self.sq2.width, 3)

    def test_x(self):
        self.assertEqual(self.sq.x, 0)
        self.assertEqual(self.sq1.x, 2)
        self.assertEqual(self.sq2.x, 0)

    def test_y(self):
        self.assertEqual(self.sq.y, 0)
        self.assertEqual(self.sq1.y, 2)
        self.assertEqual(self.sq2.y, 1)

    def test_id(self):
        self.assertEqual(self.sq.id, 1)
        self.assertEqual(self.sq1.id, 2)
        self.assertEqual(self.sq2.id, 40)

    def test_inheritance(self):
        self.assertIsInstance(self.sq, Square)
        self.assertIsInstance(self.sq, Rectangle)
        self.assertIsInstance(self.sq, Base)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_private_attr(self):
        with self.assertRaises(AttributeError):
            self.sq.__width
            self.sq.__x
            self.sq.__y


class TestValidation(unittest.TestCase):
    '''test that the corsq attr type and value is given'''

    def test_width_validation(self):
        msg = "width must be an integer"
        msg1 = "width must be > 0"
        self.assertRaisesRegex(TypeError, msg, Square, "two")
        self.assertRaisesRegex(TypeError, msg, Square, [2])
        self.assertRaisesRegex(TypeError, msg, Square, (2,))
        self.assertRaisesRegex(TypeError, msg, Square, {})
        self.assertRaisesRegex(ValueError, msg1, Square, 0)
        self.assertRaisesRegex(ValueError, msg1, Square, -1)

    def test_x_validation(self):
        msg = "x must be an integer"
        msg1 = "x must be >= 0"
        self.assertRaisesRegex(TypeError, msg, Square, 1, x="one")
        self.assertRaisesRegex(ValueError, msg1, Square, 2, x=-1)

    def test_y_validation(self):
        msg = "y must be an integer"
        msg1 = "y must be >= 0"
        self.assertRaisesRegex(TypeError, msg, Square, 1, y="one")
        self.assertRaisesRegex(ValueError, msg1, Square, 2, y=-1)


class TestAccessoryMethods(unittest.TestCase):
    '''tests accessory methods'''
    def setUp(self):
        self.sq = Square(5, test=True)
        self.sq1 = Square(7, 2, 2, test=True)
        self.sq2 = Square(3, 0, 1, 40, test=True)
        self.list_sq = [self.sq, self.sq1, self.sq2]

    def tearDown(self):
        del self.sq
        del self.sq1
        del self.sq2
        del self.list_sq

    def test_area(self):
        '''tests the area() method'''
        for sq in self.list_sq:
            self.assertEqual(sq.area(), sq.width ** 2)

    def test_display(self):
        '''tests the display() method'''
        for sq in self.list_sq:
            sq_str = ("\n" * sq.y) + ((' ' * sq.x) + (
                "#" * sq.width) + "\n") * sq.width
            self.assertEqual(sq.display(), sq_str)

    def test_string_repr(self):
        for sq in self.list_sq:
            self.assertEqual(str(sq), (
                f"[Square] ({sq.id}) {sq.x}/{sq.y}"
                f" - {sq.width}")
            )


class TestUpdateMethod(unittest.TestCase):
    '''tests the update() method in various use cases'''
    def setUp(self):
        self.sq = Square(5, test=True)
        self.sq1 = Square(7, 2, 2, test=True)
        self.sq2 = Square(3, 0, 1, 40, test=True)
        self.list_sq = [self.sq, self.sq1, self.sq2]

    def tearDown(self):
        del self.sq
        del self.sq1
        del self.sq2
        del self.list_sq

    def test_update_with_args(self):
        self.sq.update(5, 12, 3, 4)
        self.assertEqual(self.sq.id, 5)
        self.assertEqual(self.sq.width, 12)
        self.assertEqual(self.sq.x, 3)
        self.assertEqual(self.sq.y, 4)

    def test_update_with_kwargs(self):
        new_parameters = {"size": 10, "id": 50, "x": 4, "y": 6}
        self.sq1.update(**new_parameters)
        self.assertEqual(self.sq1.id, 50)
        self.assertEqual(self.sq1.width, 10)
        self.assertEqual(self.sq1.height, 10)
        self.assertEqual(self.sq1.x, 4)
        self.assertEqual(self.sq1.y, 6)


class TestSerialization(unittest.TestCase):
    '''tests all methods involved in serialization of square objects'''
    def setUp(self):
        self.sq = Square(5, test=True)
        self.sq1 = Square(7, 2, 2, test=True)
        self.sq2 = Square(3, 0, 1, 40, test=True)
        self.list_sq = [self.sq, self.sq1, self.sq2]
        self.list_dict = [sq.to_dictionary() for sq in self.list_sq]

    def tearDown(self):
        del self.sq
        del self.sq1
        del self.sq2
        del self.list_sq
        del self.list_dict

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(self.list_dict), (
                        json.dumps(self.list_dict)))

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(''), [])
        list_str = Square.to_json_string(self.list_dict)
        self.assertEqual(Square.from_json_string(list_str), self.list_dict)

    def test_save_to_file(self):
        Square.save_to_file(None)
        self.assertTrue(ospath.exists("Square.json"))
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        Square.save_to_file([])
        self.assertTrue(ospath.exists("Square.json"))
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        Square.save_to_file(self.list_sq)
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, Square.to_json_string(self.list_dict))

    def test_create(self):
        sq_dict = Square.to_dictionary(self.sq)
        sq1_dict = Square.to_dictionary(self.sq1)
        sq = Square.create(**sq_dict)
        sq1 = Square.create(**sq1_dict)
        self.assertEqual(sq, self.sq)
        self.assertEqual(sq1, self.sq1)

    def test_load_from_file(self):
        Square.save_to_file(self.list_sq)
        list_sqs = Square.load_from_file()
        self.assertEqual(list_sqs, self.list_sq)

    def test_save_to_file_csv(self):
        Square.save_to_file_csv(None)
        self.assertTrue(ospath.exists("Square.json"))
        with open("Square.csv", "r") as f:
            content = f.read()
        self.assertEqual(content, "")
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            content = f.read()
        self.assertEqual(content, "")
        Square.save_to_file_csv(self.list_sq)
        with open("Square.csv", "r") as f:
            content = f.readlines()
        for i in range(1, len(content)):
            sq = self.list_sq[i - 1]
            csv_str = f"{sq.id},{sq.width},{sq.x},{sq.y}\n"
            self.assertEqual(content[i], csv_str)

    def load_from_file_csv(self):
        Square.save_to_file_csv(self.list_sq)
        list_sqs = Square.load_from_file_csv()
        self.assertEqual(list_sqs, self.list_sq)
