import unittest
from Heimdall.connectors.postgres import PostgresConnector

class TestPostgresConnector(unittest.TestCase):
    def test_get_db(self):
        connector = PostgresConnector('postgresql://apdul@localhost:5432/postgres')

        # 테스트 메서드 호출
        schemas = connector.get_schemas()

        # 결과 확인
        expected_databases = ['schema1', 'schema2', 'schema3']
        print(schemas)
        self.assertEqual(schemas, expected_databases)


if __name__ == '__main__':
    unittest.main()
