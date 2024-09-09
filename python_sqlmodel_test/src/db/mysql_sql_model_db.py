from sqlmodel import create_engine, Session


class SQLModelDB:
    def __init__(self):
        self.host = "localhost"
        self.port = 3307
        self.user = "developer"
        self.password = "password"
        self.database = "test_db"
        self.connection = self.init_connection()
        self.session = self.init_session()

    def init_connection(self):
        connection_string = f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        engine = create_engine(connection_string, echo=True)
        return engine

    def init_session(self):
        return Session(self.connection)
