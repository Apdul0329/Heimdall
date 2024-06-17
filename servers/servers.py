import os
import grpc
from concurrent import futures

import servers.storages_pb2
import servers.storages_pb2_grpc as storages_pb2_grpc
from servers.services import DataSourceManageServiceServicer

GRPC_SERVER_ADDRESS = os.getenv('GRPC_SERVER_ADDRESS', '[::]:50051')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    storages_pb2_grpc.add_DataSourceManageServiceServicer_to_server(
        DataSourceManageServiceServicer(),
        server
    )
    server.add_insecure_port(GRPC_SERVER_ADDRESS)
    server.start()
    server.wait_for_termination()




