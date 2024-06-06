#!/usr/bin/env python3
'''unittests'''
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    '''tests a function'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b':2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, expected_res):
        '''test that the method returns what it is suppposed to'''
        self.assertEqual(access_nested_map(map, path), expected_res)

if __name__ == '__main__':
    unittest.main()