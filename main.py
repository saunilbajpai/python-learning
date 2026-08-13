from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

# Initialize FastAPI application
app = FastAPI()

# Pydantic model for Item with type validation
class item(BaseModel):
    name: str
    price: float
    isOffer: bool | None = None  # Optional boolean fiel
    email: EmailStr              # Validated email address


# Root endpoint: Returns a basic welcome message
@app.get("/")
def home():
    return {"message": "Hello FastApi"}


# Path and Query parameters demonstration:
# item_id: Required path parameter (int)
# q: Optional query parameter (str or None, defaults to None)
@app.get("/item/{item_id}/{q}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
 