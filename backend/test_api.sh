#!/bin/bash

BASE_URL="http://localhost:5000"

echo "Testing Health Check..."
curl -s $BASE_URL/
echo -e "\n"

echo "Testing User Registration..."
curl -s -X POST $BASE_URL/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"username": "tester", "email": "tester@test.com", "password": "password123"}'
echo -e "\n"

echo "Testing User Login..."
curl -s -X POST $BASE_URL/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email": "tester@test.com", "password": "password123"}'
echo -e "\n"

echo "Testing Get Auctions..."
curl -s $BASE_URL/api/auctions/
echo -e "\n"

echo "Testing Get Specific Auction..."
# Using the ID from the MockDB
curl -s $BASE_URL/api/auctions/64f1a2b3c4d5e6f7a8b9c0d5
echo -e "\n"
