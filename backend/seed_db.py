import asyncio
from app.core.db import db

async def seed():
    # Adding more mock players
    extra_players = [
        {"_id": "p3", "name": "Rohit Sharma", "category": "Batsman", "basePrice": 1800000, "status": "unsold"},
        {"_id": "p4", "name": "Jasprit Bumrah", "category": "Bowler", "basePrice": 2000000, "status": "unsold"},
        {"_id": "p5", "name": "Hardik Pandya", "category": "All-rounder", "basePrice": 1500000, "status": "unsold"},
    ]
    for p in extra_players:
        await db.insert_one("players", p)

    # Adding more mock teams
    extra_teams = [
        {"_id": "t3", "name": "MI", "budget": 100000000},
        {"_id": "t4", "name": "GT", "budget": 100000000},
    ]
    for t in extra_teams:
        await db.insert_one("teams", t)

    print("Database seeded with mock data!")

if __name__ == "__main__":
    asyncio.run(seed())
