import os
import uuid
from dotenv import load_dotenv

load_dotenv()

class MockDB:
    def __init__(self):
        self.users = []
        self.players = [
            {"_id": "64f1a2b3c4d5e6f7a8b9c0d1", "name": "Virat Kohli", "category": "Batsman", "basePrice": 2000000, "status": "unsold"},
            {"_id": "64f1a2b3c4d5e6f7a8b9c0d2", "name": "MS Dhoni", "category": "Wicketkeeper", "basePrice": 1500000, "status": "unsold"},
        ]
        self.teams = [
            {"_id": "64f1a2b3c4d5e6f7a8b9c0d3", "name": "RCB", "budget": 100000000},
            {"_id": "64f1a2b3c4d5e6f7a8b9c0d4", "name": "CSK", "budget": 100000000},
        ]
        self.auctions = [
            {"_id": "64f1a2b3c4d5e6f7a8b9c0d5", "name": "IPL 2024 Auction", "players": [], "currentPlayer": "64f1a2b3c4d5e6f7a8b9c0d1", "status": "active"}
        ]

    async def find_one(self, collection, query):
        coll = getattr(self, collection)
        for item in coll:
            match = True
            for k, v in query.items():
                if item.get(k) != v:
                    match = False
                    break
            if match: return item
        return None

    async def find_all(self, collection):
        return getattr(self, collection)

    async def insert_one(self, collection, document):
        coll = getattr(self, collection)
        if "_id" not in document or document["_id"] is None:
            document["_id"] = str(uuid.uuid4())
        coll.append(document)
        return document

db = MockDB()
