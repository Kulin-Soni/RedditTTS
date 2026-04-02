import asyncpraw as pw
from load_dotenv import load_dotenv
from os import getenv

load_dotenv(".env")
client = pw.Reddit(
    client_id=getenv("CLIENT_ID"),
    client_secret=getenv("CLIENT_SECRET"),
    password=getenv("PASSWORD"),
    user_agent=getenv("USERAGENT"),
    username=getenv("USERNAME"),
)