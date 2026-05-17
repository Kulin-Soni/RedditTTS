import asyncpraw as pw
from load_dotenv import load_dotenv
from os import environ as env

load_dotenv(".env")
client = pw.Reddit(
    client_id=env.get("CLIENT_ID"),
    client_secret=env.get("CLIENT_SECRET"),
    password=env.get("PASSWORD"),
    user_agent=env.get("USERAGENT"),
    username=env.get("USERNAME"),
)

