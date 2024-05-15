from sqlalchemy import text

from Heimdall.connectors.base import BaseConnector


GET_DB_QUERY = text('SHOW DATABASES')


class MySQLConnector(BaseConnector):
    def __init__(self, uri):
        super(MySQLConnector, self).__init__(uri)

    def get_db(self):
        with self.connection:
            result = self.connection.execute(GET_DB_QUERY).fetchall()
            databases = [row[0] for row in result]
        return databases

