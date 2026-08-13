from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "FastAPI is working"}


@app.get("/test-db")
async def test_db():
    async with engine.connect() as connection:
        result = await connection.execute(text("SELECT 1"))

    return {"database": result.scalar()}