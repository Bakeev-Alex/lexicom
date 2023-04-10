from fastapi import FastAPI
from phone_book import routers as phone_book

app = FastAPI()

app.include_router(phone_book.router)
