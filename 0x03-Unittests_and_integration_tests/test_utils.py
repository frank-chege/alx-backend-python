#!/usr/bin/env python3
'''unittests'''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch

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

    @parameterized.expand([
        ({}, ('a',)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, path):
        '''test if a keyerror is raised'''
        with self.assertRaises(KeyError):
            access_nested_map(map, path)
    
class TestGetJson(unittest.TestCase):
    @patch('requests.get')
    def test_get_json(self, mock_get):
        # Set the return value for the mocked requests.get
        mock_get.return_value.json.return_value = {"payload": True}

        # Call your function
        result = get_json('http://example.com')

        # Assertions
        self.assertEqual(result, {"payload": True})
        mock_get.assert_called_once_with('http://example.com')


if __name__ == '__main__':
    unittest.main()