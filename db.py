from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from db_conf import db_settings as settings

Base = declarative_base()

def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, echo=True)
    return engine

engine = get_engine(
    settings.get('username'),
    settings.get('password'),
    settings.get('host'),
    settings.get('port'),
    settings.get('pgdb')
)

SessionLocal = sessionmaker(bind=engine)
