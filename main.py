from fastapi import FastAPI, HTTPException, Path, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel
from typing import Annotated
import models  

app = FastAPI()

URL_DATABASE = ''
engine = create_engine(URL_DATABASE)

@app.get("/introduction")
def introduction_page():
    return {"message":"this is a backend project for patients database for a hospital"}

