# Cricket Auction Application

Full-stack cricket auction application with live bidding, built with FastAPI and React.

## Project Structure

- `backend/`: FastAPI Python application.
- `frontend/`: React application.

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm

## How to Run

### Backend

1. Navigate to the `backend/` directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn app.main:socket_app --host 0.0.0.0 --port 5000 --reload
   ```
   The API will be available at `http://localhost:5000`.
   API Documentation (Swagger UI) is available at `http://localhost:5000/docs`.

### Frontend

1. Navigate to the `frontend/` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```
   The app will be available at `http://localhost:3000`.

## Testing the API

You can use the provided script to test the API endpoints:
```bash
cd backend
./test_api.sh
```

## Mock Data

The backend uses an in-memory database (`MockDB`) by default for easy testing in the sandbox. To populate it with more data, you can use the `seed_db.py` script (if implementing a persistent DB later).
