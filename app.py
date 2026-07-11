from fastapi import FastAPI
from src.routes.contact import route as contact_route

app = FastAPI(title="Contact API")

app.include_router(contact_route)

@app.get("/")
def home():
    return 'Welcome to contact API'