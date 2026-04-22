import React, { useState, useEffect, useMemo } from 'react';
import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import io from 'socket.io-client';
import axios from 'axios';
import './AuctionRoom.css';

const AuctionScreen = () => {
  const { id: auctionId } = useParams();
  const [auction, setAuction] = useState(null);
  const [bids, setBids] = useState([]);
  const [currentBid, setCurrentBid] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const userLogin = useSelector((state) => state.user);
  const { userInfo } = userLogin;

  const socket = useMemo(() => io('http://localhost:5000'), []);

  useEffect(() => {
    const fetchAuction = async () => {
      try {
        const { data } = await axios.get(`/api/auctions/${auctionId}`);
        setAuction(data);
        if (data.currentPlayer) {
          setCurrentBid(data.currentPlayer.currentBid || data.currentPlayer.basePrice);
        }
        setLoading(false);
      } catch (err) {
        setError(err.response?.data?.message || err.message);
        setLoading(false);
      }
    };

    fetchAuction();

    socket.emit('joinAuction', auctionId);

    socket.on('newBid', (bid) => {
      setBids((prevBids) => [...prevBids, bid]);
      setCurrentBid(bid.amount);
    });

    socket.on('playerSold', ({ player, team }) => {
      // Handle player sold logic
      fetchAuction(); // Refresh auction state
    });

    return () => {
      socket.emit('leaveAuction', auctionId);
      socket.off('newBid');
      socket.off('playerSold');
    };
  }, [auctionId, socket]);

  const placeBid = () => {
    if (auction && auction.currentPlayer) {
      const playerId = auction.currentPlayer._id;
      const teamId = userInfo?.team || '64f1a2b3c4d5e6f7a8b9c0d1'; // Mock team ID if not logged in
      const amount = (currentBid || auction.currentPlayer.basePrice) + 1000;
      socket.emit('bid', { auctionId, playerId, teamId, amount });
    }
  };

  return (
    <div className="container mt-4">
      {loading ? (
        <div className="text-center">
          <div className="spinner-border" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      ) : error ? (
        <div className="alert alert-danger">Error: {error}</div>
      ) : auction ? (
        <div className="card shadow">
          <div className="card-header bg-primary text-white">
            <h2 className="mb-0">{auction.name}</h2>
          </div>
          <div className="card-body">
            {auction.currentPlayer ? (
              <div className="row">
                <div className="col-md-6">
                  <div className="player-card p-3 border rounded bg-light">
                    <h3 className="text-primary">{auction.currentPlayer.name}</h3>
                    <p className="lead mb-1">Category: <strong>{auction.currentPlayer.category}</strong></p>
                    <p className="lead">Base Price: <strong>₹{auction.currentPlayer.basePrice.toLocaleString()}</strong></p>
                    <hr />
                    <div className="bid-section text-center py-3">
                      <h4 className="text-muted">Current Bid</h4>
                      <h1 className="display-4 text-success">₹{(currentBid || auction.currentPlayer.basePrice).toLocaleString()}</h1>
                      <button
                        className="btn btn-success btn-lg px-5 mt-3 shadow"
                        onClick={placeBid}
                      >
                        RAISE BID (+₹1,000)
                      </button>
                    </div>
                  </div>
                </div>
                <div className="col-md-6">
                  <div className="bid-history p-3 border rounded shadow-sm bg-white" style={{ height: '400px', overflowY: 'auto' }}>
                    <h4 className="border-bottom pb-2">Bid History</h4>
                    <ul className="list-group list-group-flush">
                      {bids.slice().reverse().map((bid, index) => (
                        <li key={index} className="list-group-item d-flex justify-content-between align-items-center">
                          <span>{bid.teamName}</span>
                          <span className="badge bg-success rounded-pill">₹{bid.amount.toLocaleString()}</span>
                        </li>
                      ))}
                      {bids.length === 0 && <p className="text-muted text-center mt-4">No bids yet. Be the first!</p>}
                    </ul>
                  </div>
                </div>
              </div>
            ) : (
              <div className="text-center py-5">
                <h3 className="text-muted">No active player in this auction.</h3>
              </div>
            )}
          </div>
        </div>
      ) : (
        <div className="alert alert-warning">Auction not found.</div>
      )}
    </div>
  );
};

export default AuctionScreen;