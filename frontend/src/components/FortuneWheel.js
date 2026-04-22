import React, { useState } from 'react';
import './FortuneWheel.css';

const FortuneWheel = ({ items, onSelect }) => {
  const [spinning, setSpinning] = useState(false);
  const [result, setResult] = useState(null);

  const spin = () => {
    if (spinning) return;
    setSpinning(true);
    const randomIndex = Math.floor(Math.random() * items.length);
    setTimeout(() => {
      setSpinning(false);
      setResult(items[randomIndex]);
      onSelect(items[randomIndex]);
    }, 3000);
  };

  return (
    <div className="fortune-wheel-container">
      <div className={`wheel ${spinning ? 'spinning' : ''}`}>
        {items.map((item, index) => (
          <div key={index} className="wheel-item">
            {item.name}
          </div>
        ))}
      </div>
      <button onClick={spin} disabled={spinning}>
        Spin the Wheel
      </button>
      {result && <p>Result: {result.name}</p>}
    </div>
  );
};

export default FortuneWheel;
