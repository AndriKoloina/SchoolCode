from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor


app = FastAPI()

database_config = {
    "dbname" : "backendDatabase",
    "user" : "postgres",
    "password" : "0000",
    "host" : "localhost",
    "port" : "5432"
}

