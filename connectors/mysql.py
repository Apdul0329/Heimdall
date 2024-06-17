from sqlalchemy import Table
from sqlalchemy.sql import select

from connectors.base import BaseConnector


class MySQLConnector(BaseConnector):
    def __init__(self, uri):
        super(MySQLConnector, self).__init__(uri)

    def get_schemas(self):
        return self.inspector.get_schema_names()

    def get_tables(self, database):
        return self.inspector.get_table_names(schema=database)

    def get_columns(self, database, table):
        return self.inspector.get_columns(
            table_name=table,
            schema=database
        )

    def get_data(self, schema, table, row_count, columns=None):
        if schema not in self.get_schemas():
            raise ValueError(f"Schema '{schema}' does not exist.")

        if table not in self.get_tables(schema):
            raise ValueError(f"Table '{table}' does not exist in schema '{schema}'.")

        table_view = Table(table, self.metadata, autoload_with=self.engine, schema=schema)

        if columns:
            selected_columns = [table_view.c[column] for column in columns]
            query = select(*selected_columns).limit(row_count)
        else:
            query = select(table_view).limit(row_count)

        with self.engine.connect() as connection:
            result = connection.execute(query)
            rows = result.fetchall()
        return rows

