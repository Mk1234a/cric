import React, { useState, useEffect } from 'react';
import axios from 'axios';
import FortuneWheel from '../components/FortuneWheel';

const HomeScreen = () => {
  const [auctions, setAuctions] = useState([]);
  const [teams, setTeams] = useState([
    { name: 'Team A' },
    { name: 'Team B' },
    { name: 'Team C' },
  ]);

  useEffect(() => {
    const fetchAuctions = async () => {
      try {
        const { data } = await axios.get('/api/auctions');
        setAuctions(data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchAuctions();
  }, []);

  return (
    <div className="container mt-5">
      <h1>Live Cricket Auction</h1>
      <div className="row">
        <div className="col-md-8">
          <h2>Today's Auctions</h2>
          {auctions.length === 0 ? (
            <p>No active auctions today.</p>
          ) : (
            <ul>
              {auctions.map((auction) => (
                <li key={auction._id}>{auction.name}</li>
              ))}
            </ul>
          )}
          <h2 className="mt-4">Upcoming Auctions</h2>
          <p>Stay tuned for upcoming tournaments!</p>
        </div>
        <div className="col-md-4">
          <h2>Lucky Draw (Fortune Wheel)</h2>
          <FortuneWheel items={teams} onSelect={(team) => console.log(team)} />
        </div>
      </div>
    </div>
  );
};

export default HomeScreen;
