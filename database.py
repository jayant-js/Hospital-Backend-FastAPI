import pymysql
from sqlmodel import create_engine, Session
from fastapi import Depends

URL_DATABASE = "mysql+pymysql://root:abhi@localhost:3306/hospital_db"

engine = create_engine(URL_DATABASE,echo=True)

def get_session():
    with Session(engine) as session:
        yield session