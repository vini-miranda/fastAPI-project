from typing import list
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from mysql import connector

class Settings(BaseSettings):

    API_V1_STR: str = '/api/v1'
    DB_URL: str = ''
    DB_BASE_MODEL = declarative_base()

    class Config: 
        case_sensitive = True

settings = Settings()

mydb = connector.connect(
    host = "127.0.0.1:3306",
    user="root",
    password="root"
)

print(mydb)