from fastapi import APIRouter, HTTPException
from app.models.schemas import Auction
from app.core.db import db

router = APIRouter()

@router.get("/")
async def get_auctions():
    return await db.find_all("auctions")

@router.get("/{id}")
async def get_auction(id: str):
    auction = await db.find_one("auctions", {"_id": id})
    if not auction:
        raise HTTPException(status_code=404, detail="Auction not found")

    if auction.get("currentPlayer"):
        player = await db.find_one("players", {"_id": auction["currentPlayer"]})
        auction["currentPlayer"] = player

    return auction
