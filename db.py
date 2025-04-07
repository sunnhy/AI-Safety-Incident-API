from pymongo import MongoClient # type: ignore
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("Newton-AI")]
incidents_collection = db["incidents"]

