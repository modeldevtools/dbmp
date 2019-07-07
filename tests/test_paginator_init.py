import unittest
import sqlite3
from paginator import QueryPaginator


class TestSQLitePaginatorInit(unittest.TestCase):
    """Testing QueryPaginator.__init__()"""

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn_file = sqlite3.connect('nw.sqlite')

    def tearDown(self):
        self.conn.close()
        self.conn_file.close()

    def test_noquery(self):
        """No query supplied to __init__()"""
        with self.assertRaises(ValueError):
            QueryPaginator(query='', connection=self.conn)

    def test_query_not_str(self):
        """Query is not of type string"""
        with self.assertRaises(ValueError):
            QueryPaginator(query=22, connection=self.conn)

    def test_noconnection(self):
        """No connection supplied to __init__()"""
        with self.assertRaises(ValueError):
            QueryPaginator(query='dumb query', connection=None)

    def test_badconnection(self):
        """Connection is of unexpected type"""
        with self.assertRaises(ValueError):
            QueryPaginator(query='dumb query', connection='dumb')

    def test_all_is_good(self):
        """Query and Connection are both good"""
        query = "select * from 'order'"
        paginator = QueryPaginator(query=query, connection=self.conn_file)
        self.assertIsInstance(paginator, QueryPaginator)


if __name__ == "__main__":
    unittest.main()
