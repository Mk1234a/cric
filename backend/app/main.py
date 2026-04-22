from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import users, auctions
from app.socket.auction_socket import init_socket
import socketio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(auctions.router, prefix="/api/auctions", tags=["auctions"])

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
socket_app = socketio.ASGIApp(sio, app)

@app.on_event("startup")
async def startup_event():
    await init_socket(sio)

@app.get("/")
async def root():
    return {"message": "Cricket Auction FastAPI is running"}
