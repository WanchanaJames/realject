from fastapi import FastAPI
from config import engine

import tables.users as user_table

user_table.Base.metadata.create_all(bind=engine)
app = FastAPI()

#@app.get("/")
#async def roof():
#    return "Hello World"