from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

class DatabaseManager:
    def __init__(self, user='root', password='rootpass', host='localhost', port='3306', db='templates_db'):
        self.engine = self.create_engine(user, password, host, port, db)
        self.Session = sessionmaker(bind=self.engine)

    def create_engine(self, user, password, host, port, db):
        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        return create_engine(url, echo=True)

    def create_session(self):
        return self.Session()

    def close_session(self, session):
        session.close()

    def check_connection(self, session):
        try:
            session.execute(text("SELECT 1"))
            print("Connection to the database is successful.")
        except SQLAlchemyError as e:
            print(f"Error during connection: {str(e)}")
