import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

class DataLoader:
    def __init__(self):
        load_dotenv()
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        host = os.getenv("HOST")
        port = os.getenv("PORT")
        database = os.getenv("DATABASE")
        db_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(db_url)
        
    def load_data(self, table_name: str):
        # TODO: to change later based on our needs
        return pd.read_sql(f"SELECT * FROM {table_name} LIMIT 10;", self.engine)