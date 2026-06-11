from fastapi import FastAPI
from database import engine

app = FastAPI()

@app.on_event("startup")
def startup():
    try:
        conn = engine.connect()
        print("Connected to PostgreSQL successfully!")
        conn.close()
    except Exception as e:
        print("DB connection failed:", e)

@app.get("/")
def home():
    return {"message": "FastAPI running with proper DB startup hook"}
