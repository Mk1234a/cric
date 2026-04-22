from app.core.db import db

async def init_socket(sio):
    @sio.on('joinAuction')
    async def join_auction(sid, auction_id):
        await sio.enter_room(sid, auction_id)
        print(f"User {sid} joined auction {auction_id}")

    @sio.on('bid')
    async def handle_bid(sid, data):
        auction_id = data.get('auctionId')
        player_id = data.get('playerId')
        team_id = data.get('teamId')
        amount = data.get('amount')

        team_name = "Unknown Team"
        team = await db.find_one("teams", {"_id": team_id})
        if team: team_name = team["name"]

        bid_data = {
            "auctionId": auction_id,
            "playerId": player_id,
            "teamId": team_id,
            "teamName": team_name,
            "amount": amount
        }
        await sio.emit('newBid', bid_data, room=auction_id)
