import os
from dotenv import load_dotenv
from app.adapters.database.postgres_database import PostgresDB

load_dotenv()
DATABASE_URI = os.getenv('DATABASE_URI')

db = PostgresDB(DATABASE_URI)
db.initialize_db()
