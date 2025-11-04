
from src.database.connection import engine



class DBClient:
    def execute_one(self, query):
        try:
            with engine.begin() as conn:
                row = conn.execute(query).fetchone()
                if row:
                    return row
        except Exception:
            raise ValueError("Data base execute error")

    def execute_all(self, query):
        try:
            with engine.begin() as conn:
                row = conn.execute(query).fetchall()
                if row:
                    return row
        except Exception:
            raise ValueError("Data base execute error")
    
    
            
