import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:secret123@postgres-db:5432/appdb"
)

engine = create_engine(DATABASE_URL)

