from sqlalchemy import create_engine
from sqlalchemy import MetaData
from src.utlis.config import get_database_url


engine = create_engine(get_database_url())

metadata = MetaData()

metadata.bind=engine