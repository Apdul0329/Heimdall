from sqlalchemy import text

from Heimdall.connectors.base import BaseConnector

GET_SCHEMA_QUERY = text('select nspname from pg_catalog.pg_namespace')


class PostgresConnector(BaseConnector):
    def __init__(self, uri):
        super(PostgresConnector, self).__init__(uri)

    def get_schemas(self):
        with self.connection:
            result = self.connection.execute(GET_SCHEMA_QUERY).fetchall()
            schemas = [row[0] for row in result]
        return schemas


