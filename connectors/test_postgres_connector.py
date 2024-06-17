import unittest
from Heimdall.connectors.postgres import PostgresConnector
from Heimdall.connectors.mysql import MySQLConnector

class TestPostgresConnector(unittest.TestCase):
    def test_get_db(self):
        # connector = PostgresConnector('postgresql://apdul@localhost:5432/alpacon')
        connector = MySQLConnector('mysql://root:root@localhost:3306')

        # 테스트 메서드 호출
        # schemas = connector.get_schemas()
        # schemas = connector.get_db()
        tables = connector.get_tables('information_schema')
        # tables = connector.get_tables('public')
        # columns = connector.get_columns('information_schema', 'sql_parts')
        # columns = connector.get_columns('public', 'servers_server')
        # data = connector.get_data(
        #     schema='public',
        #     table='servers_server',
        #     row_count=10
        # )

        # 결과 확인
        # print(schemas)
        print(tables)
        # print(columns)
        # for column in columns:
        #     print(str(column['type']))
        # for column in columns:
        #     print(column['type'].name)
        #     print(column['type'].data_type)
        # print(data)


if __name__ == '__main__':
    unittest.main()
