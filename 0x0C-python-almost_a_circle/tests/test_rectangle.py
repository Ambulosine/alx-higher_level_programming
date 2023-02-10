#!/usr/bin/python3
'''unittest file for rectangle module'''
from models.rectangle import Rectangle
from models.base import Base
import unittest
import json
from os import path as ospath


class TestInstantiation(unittest.TestCase):
    '''tests instantiation of rect objects'''

    def setUp(self):
        self.rect = Rectangle(5, 6, test=True)
        self.rect1 = Rectangle(7, 12, 2, 2, test=True)
        self.rect2 = Rectangle(3, 5, 0, 1, 40, test=True)

    def tearDown(self):
        del self.rect
        del self.rect1
        del self.rect2

    def test_width(self):
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect1.width, 7)
        self.assertEqual(self.rect2.width, 3)

    def test_height(self):
        self.assertEqual(self.rect.height, 6)
        self.assertEqual(self.rect1.height, 12)
        self.assertEqual(self.rect2.height, 5)

    def test_x(self):
        self.assertEqual(self.rect.x, 0)
        self.assertEqual(self.rect1.x, 2)
        self.assertEqual(self.rect2.x, 0)

    def test_y(self):
        self.assertEqual(self.rect.y, 0)
        self.assertEqual(self.rect1.y, 2)
        self.assertEqual(self.rect2.y, 1)

    def test_id(self):
        self.assertEqual(self.rect.id, 1)
        self.assertEqual(self.rect1.id, 2)
        self.assertEqual(self.rect2.id, 40)

    def test_inheritance(self):
        self.assertIsInstance(self.rect, Rectangle)
        self.assertIsInstance(self.rect, Base)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_private_attr(self):
        with self.assertRaises(AttributeError):
            self.rect.__width
            self.rect.__height
            self.rect.__x
            self.rect.__y


class TestValidation(unittest.TestCase):
    '''test that the correct attr type and value is given'''

    def test_width_validation(self):
        msg = "width must be an integer"
        msg1 = "width must be > 0"
        self.assertRaisesRegex(TypeError, msg, Rectangle, "two", 5)
        self.assertRaisesRegex(TypeError, msg, Rectangle, [2], 5)
        self.assertRaisesRegex(TypeError, msg, Rectangle, (2,), "five")
        self.assertRaisesRegex(TypeError, msg, Rectangle, {}, 5)
        self.assertRaisesRegex(ValueError, msg1, Rectangle, 0, 5)
        self.assertRaisesRegex(ValueError, msg1, Rectangle, -1, 5)

    def test_height_validation(self):
        msg = "height must be an integer"
        msg1 = "height must be > 0"
        self.assertRaisesRegex(TypeError, msg, Rectangle, 5, "two")
        self.assertRaisesRegex(TypeError, msg, Rectangle, 5, [2])
        self.assertRaisesRegex(TypeError, msg, Rectangle, 5, (2,))
        self.assertRaisesRegex(TypeError, msg, Rectangle, 5, {})
        self.assertRaisesRegex(ValueError, msg1, Rectangle, 5, 0)
        self.assertRaisesRegex(ValueError, msg1, Rectangle, 5, -1)

    def test_x_validation(self):
        msg = "x must be an integer"
        msg1 = "x must be >= 0"
        self.assertRaisesRegex(TypeError, msg, Rectangle, 1, 2, x="one")
        self.assertRaisesRegex(ValueError, msg1, Rectangle, 1, 2, x=-1)

    def test_y_validation(self):
        msg = "y must be an integer"
        msg1 = "y must be >= 0"
        self.assertRaisesRegex(TypeError, msg, Rectangle, 1, 2, y="one")
        self.assertRaisesRegex(ValueError, msg1, Rectangle, 1, 2, y=-1)


class TestAccessoryMethods(unittest.TestCase):
    '''tests accessory methods'''
    def setUp(self):
        self.rect = Rectangle(5, 6, test=True)
        self.rect1 = Rectangle(7, 4, 2, 2, test=True)
        self.rect2 = Rectangle(3, 5, 0, 1, 40, test=True)
        self.list_rect = [self.rect, self.rect1, self.rect2]

    def tearDown(self):
        del self.rect
        del self.rect1
        del self.rect2
        del self.list_rect

    def test_area(self):
        '''tests the area() method'''
        for rect in self.list_rect:
            self.assertEqual(rect.area(), (
                rect.width * rect.height))

    def test_display(self):
        '''tests the display() method'''
        for rect in self.list_rect:
           rect_str = ("\n" * rect.y) + ((' ' * rect.x) + (
                "#" * rect.width) + "\n") * rect.height
            self.assertEqual(rect.display(), rect_str)

    def test_string_repr(self):
        for rect in self.list_rect:
            self.assertEqual(str(rect), (
                f"[Rectangle] ({rect.id}) {rect.x}/{rect.y}"
                f" - {rect.width}/{rect.height}")
            )

    def test_to_dictionary(self):
        for rect in self.list_rect:
            self.assertEqual(rect.to_dictionary(), eval(
                f"{{'width': {rect.width}, 'height': {rect.height},"
                f"'id': {rect.id}, 'x': {rect.x}, 'y':{rect.y}}}")
            )


class TestUpdateMethod(unittest.TestCase):
    '''tests the update() method in various use cases'''
    def setUp(self):
        self.rect = Rectangle(5, 6, test=True)
        self.rect1 = Rectangle(7, 4, 2, 2, test=True)
        self.rect2 = Rectangle(3, 5, 0, 1, 40, test=True)
        self.list_rect = [self.rect, self.rect1, self.rect2]

    def tearDown(self):
        del self.rect
        del self.rect1
        del self.rect2
        del self.list_rect

    def test_update_with_args(self):
        self.rect.update(5, 12, 15, 3, 4)
        self.assertEqual(self.rect.id, 5)
        self.assertEqual(self.rect.width, 12)
        self.assertEqual(self.rect.height, 15)
        self.assertEqual(self.rect.x, 3)
        self.assertEqual(self.rect.y, 4)

    def test_update_with_kwargs(self):
        new_parameters = {"width": 10, "id": 50, "height": 5, "x": 4, "y": 6}
        self.rect1.update(**new_parameters)
        self.assertEqual(self.rect1.id, 50)
        self.assertEqual(self.rect1.width, 10)
        self.assertEqual(self.rect1.height, 5)
        self.assertEqual(self.rect1.x, 4)
        self.assertEqual(self.rect1.y, 6)


class TestSerialization(unittest.TestCase):
    '''tests all methods involved in serialization of rect objects'''
    def setUp(self):
        self.rect = Rectangle(5, 6, test=True)
        self.rect1 = Rectangle(7, 4, 2, 2, test=True)
        self.rect2 = Rectangle(3, 5, 0, 1, 40, test=True)
        self.list_rect = [self.rect, self.rect1, self.rect2]
        self.list_dict = [rect.to_dictionary() for rect in self.list_rect]

    def tearDown(self):
        del self.rect
        del self.rect1
        del self.rect2
        del self.list_rect
        del self.list_dict

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(self.list_dict), (
                        json.dumps(self.list_dict)))

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(''), [])
        list_str = Rectangle.to_json_string(self.list_dict)
        self.assertEqual(Rectangle.from_json_string(list_str), self.list_dict)

    def test_save_to_file(self):
        Rectangle.save_to_file(None)
        self.assertTrue(ospath.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        Rectangle.save_to_file([])
        self.assertTrue(ospath.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        Rectangle.save_to_file(self.list_rect)
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, Rectangle.to_json_string(self.list_dict))

    def test_create(self):
        rect_dict = Rectangle.to_dictionary(self.rect)
        rect1_dict = Rectangle.to_dictionary(self.rect1)
        rect = Rectangle.create(**rect_dict)
        rect1 = Rectangle.create(**rect1_dict)
        self.assertEqual(rect, self.rect)
        self.assertEqual(rect1, self.rect1)

    def test_load_from_file(self):
        Rectangle.save_to_file(self.list_rect)
        list_rects = Rectangle.load_from_file()
        self.assertEqual(list_rects, self.list_rect)

    def test_save_to_file_csv(self):
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as f:
            content = f.read()
        self.assertEqual(content, "")
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as f:
            content = f.read()
        self.assertEqual(content, "")
        Rectangle.save_to_file_csv(self.list_rect)
        with open("Rectangle.csv", "r") as f:
            content = f.readlines()
        for i in range(1, len(content)):
            rect = self.list_rect[i - 1]
            csv_str = (
                      f"{rect.id},{rect.width},{rect.height},"
                      f"{rect.x},{rect.y}\n")
            self.assertEqual(content[i], csv_str)

    def load_from_file_csv(self):
        Rectangle.save_to_file_csv(self.list_rect)
        list_rects = Rectangle.load_from_file_csv()
        self.assertEqual(list_rects, self.list_rect) 
