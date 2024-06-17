from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.orm import Session


class BaseConnector:
    def __init__(self, uri):
        self.engine = create_engine(uri, echo=True)
        self.connection = self.engine.connect()
        self.session = Session(self.engine)
        self.inspector = inspect(self.engine)
        self.metadata = MetaData()
