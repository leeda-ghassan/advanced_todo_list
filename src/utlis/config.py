from dotenv import load_dotenv
import os
load_dotenv()

DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")

def get_database_url():
    return f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
