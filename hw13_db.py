import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(f'postgresql+psycopg2://{os.environ.get("DB_user")}:{os.environ.get("DB_password")}'
                       f'@{os.environ.get("DB_HOST", "127.0.0.1")}:5432/postgres_db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)