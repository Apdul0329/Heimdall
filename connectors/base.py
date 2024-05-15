from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class BaseConnector:
    def __init__(self, uri):
        self.engine = create_engine(uri, echo=True)
        self.connection = self.engine.connect()
        self.session = Session(self.engine)
