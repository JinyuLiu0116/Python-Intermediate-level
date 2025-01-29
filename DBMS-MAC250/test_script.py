import unittest
from unittest.mock import patch, MagicMock
import mysql.connector

import test_MAC250_LAB_1


class TestConnection(unittest.TestCase):
    def setUp(self):
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor

    @patch('mysql.connector.connect') #Mock the MySQL connection
    def test_connection_and_query(self, mock_connect):
        """Test database connection and query execution"""
        mock_connect.return_value = self.mock_conn

        self.mock_cursor.fetchall.return_value = [
            ('AT94', 'Iron', 24.95),
            ('BV06', 'Home Gym', 794.95),
            ('CD52', 'Microwave Oven', 165.00)
        ]

        result = test_MAC250_LAB_1.execute_query('SELECT * FROM part;')

        mock_connect.assert_called_once()
        self.mock_conn.cursor.assert_called_once()
        self.mock_cursor.execute.assert_called_once_with('SELECT partNum, description, price FROM part;')
        self.mock_cursor.fetchall.assert_called_once()
        self.assertEqual(result, [
            ('AT94', 'Iron', 24.95),
            ('BV06', 'Home Gym', 794.95),
            ('CD52', 'Microwave Oven', 165.00)
        ])
if __name__=='__main__':
    unittest.main()
