import os
import json
import uuid
import grpc
import requests
import websockets
import asyncio
import pickle

import servers.storages_pb2 as storages_pb2
import servers.storages_pb2_grpc as storages_pb2_grpc
from connectors.postgres import PostgresConnector
from connectors.mysql import MySQLConnector

STORAGE_SERVICE_BASE_URL = os.getenv('STORAGE_SERVICE_BASE_URL', 'http://localhost:8080')
KAFKA_CONNECT_URL = os.getenv('KAFKA_CONNECT_URL', 'http://localhost:8083/connectors')


async def send_column_data(data):
    id = uuid.uuid4()
    WEBSOCKET_URL = STORAGE_SERVICE_BASE_URL.replace('http', 'ws') + f'/ws/columns/{id}/'
    async with websockets.connect(WEBSOCKET_URL) as websocket:
        for item in data:
            message = json.dumps(item)
            await websocket.send(message)
        await websocket.send(json.dumps({
            'signal': 'END'
        }))

def create_connector(name, cofig):
    data = {
        'name': name,
        'config': cofig
    }
    response = requests.post(
        url=KAFKA_CONNECT_URL,
        headers={'Content-Type': 'application/json'},
        json=data
    )
    if response.status_code == 201:
        return f"Connector '{name}' created successfully."
    else:
        return f"Failed to create connector '{name}'."


class DataSourceManageServiceServicer(storages_pb2_grpc.DataSourceManageServiceServicer):
    def GetSchemas(self, request, context):
        try:
            id = request.id
            vendor = request.vendor
            uri = request.uri

            if id is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "ID is required.")
            if vendor is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Vendor is required.")
            if uri is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "URI is required.")

            if vendor == 'postgresql':
                connector = PostgresConnector(uri)
            elif vendor == 'mysql':
                connector = MySQLConnector(uri)
            else:
                context.abort(grpc.StatusCode.UNIMPLEMENTED, f"{vendor} is not supported.")

            schemas = connector.get_schemas()
            data = []
            schema_protos = []
            for schema in schemas:
                data.append({
                    'storage_id': id,
                    'name': schema,
                })
                schema_protos.append(storages_pb2.Schema(
                    schema=schema
                ))

            response = requests.post(
                STORAGE_SERVICE_BASE_URL + '/schemas/',
                json=data
            )

            return storages_pb2.SchemaResponse(
                success=True,
                schemas=schema_protos
            )
        except Exception as e:
            context.abort(grpc.StatusCode.ABORTED, str(e))

    def GetTables(self, request, context):
        try:
            vendor = request.vendor
            uri = request.uri
            schemas = request.schemas

            if vendor is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Vendor is required.")
            if uri is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "URI is required.")
            if schemas is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Schema is required.")

            if vendor == 'postgresql':
                connector = PostgresConnector(uri)
            elif vendor == 'mysql':
                connector = MySQLConnector(uri)
            else:
                context.abort(grpc.StatusCode.UNIMPLEMENTED, f"{vendor} is not supported.")

            data = []
            table_protos = []
            print(schemas)
            for schema in schemas:
                print(schema)
                tables = connector.get_tables(schema.schema)
                print(tables)
                for table in tables:
                    data.append({
                        'schema_id': schema.id,
                        'name': table,
                    })
                    table_protos.append(storages_pb2.Table(
                        schema=schema.schema,
                        table=table,
                    ))

            response = requests.post(
                STORAGE_SERVICE_BASE_URL + '/tables/',
                json=data
            )

            return storages_pb2.TableResponse(
                success=True,
                tables=table_protos
            )
        except Exception as e:
            context.abort(grpc.StatusCode.ABORTED, str(e))

    def GetColumns(self, request, context):
        try:
            vendor = request.vendor
            uri = request.uri
            tables = request.tables

            if vendor is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Vendor is required.")
            if uri is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "URI is required.")
            if tables is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Table is required.")

            if vendor == 'postgresql':
                connector = PostgresConnector(uri)
            elif vendor == 'mysql':
                connector = MySQLConnector(uri)
            else:
                context.abort(grpc.StatusCode.UNIMPLEMENTED, f"{vendor} is not supported.")

            data = []
            column_protos = []
            for table in tables:
                columns = connector.get_columns(table.schema, table.table)

                for column in columns:
                    name = column.pop('name')
                    type = str(column.pop('type'))
                    data.append({
                        'table_id': table.id,
                        'name': name,
                        'type': type,
                        'details': column
                    })
                    column_protos.append(storages_pb2.Column(
                        column=name,
                    ))

            asyncio.run(send_column_data(data))
            return storages_pb2.ColumnResponse(
                success=True,
                columns=column_protos
            )
        except Exception as e:
            context.abort(grpc.StatusCode.ABORTED, str(e))

    def GetViews(self, request, context):
        try:
            vendor = request.vendor
            uri = request.uri
            schema = request.schema
            table = request.table
            columns = request.columns
            row = request.row

            if vendor is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Vendor is required.")
            if uri is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "URI is required.")
            if schema is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Schema is required.")
            if table is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Table is required.")
            if row is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Row is required.")

            if vendor == 'postgresql':
                connector = PostgresConnector(uri)
            elif vendor == 'mysql':
                connector = MySQLConnector(uri)
            else:
                context.abort(grpc.StatusCode.UNIMPLEMENTED, f"{vendor} is not supported.")

            rows = connector.get_data(schema, table, row, columns)
            return storages_pb2.ViewResponse(
                success=True,
                records=pickle.dumps(rows)
            )
        except Exception as e:
            context.abort(grpc.StatusCode.ABORTED, str(e))

    def DoMigration(self, request, context):
        try:
            source_uri = request.source_uri
            destination_uri = request.destination_uri
            table = request.table

            if source_uri is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Source URI is required.")
            if destination_uri is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Destination URI is required.")
            if table is None:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Table is required.")

            source_connector_name = str(uuid.uuid4())
            sink_connector_name = str(uuid.uuid4())
            source_connector_config = {
                'name': source_connector_name,
                'connector.class': 'io.confluent.connect.jdbc.JdbcSourceConnector',
                'tasks.max': '1',
                'connection.url': f'jdbc:{source_uri}',
                'table.whitelist': table,
                'mode': 'bulk',
                'key.converter': 'org.apache.kafka.connect.json.JsonConverter',
                'value.converter': 'org.apache.kafka.connect.json.JsonConverter',
                'key.converter.schemas.enable': 'false',
                'value.converter.schemas.enable': 'false',
            }
            sink_connector_config = {
                'name': sink_connector_name,
                'connector.class': 'io.confluent.connect.jdbc.JdbcSinkConnector',
                'tasks.max': '1',
                'connection.url': f'jdbc:{destination_uri}',
                'topics': table,
                'auto.create': 'true'
            }

            source_message = create_connector(source_connector_name, source_connector_config)
            sink_message = create_connector(sink_connector_name, sink_connector_config)

            return storages_pb2.MigrationResponse(
                success=True,
                message=f'{source_message}\n{sink_message}'
            )
        except Exception as e:
            context.abort(grpc.StatusCode.ABORTED, str(e))