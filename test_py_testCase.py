# JawnPythias
# date:22/02/2024

import unittest
from py_testCase import Employee

class testEmployee(unittest.TestCase):
    def setUp(self):
        self.xiaoming = Employee("111", "222", 3000)

    def test_give_default_raise(self):
        self.xiaoming.give_raise()
        self.assertEqual(self.xiaoming.salary, 8000)

    def test_give_custom_raise(self):
        self.xiaoming.give_raise(10000)
        self.assertEqual(self.xiaoming.salary, 13000)
