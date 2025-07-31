#!/bin/bash

# Exit script immediately if any command fail

PROJECT_DIR=~/my-portfolio
cd "$PROJECT_DIR"

echo "Fetching latest changes from GitHub..."
git fetch
git reset origin/main --hard

echo "Activating virtual environment..."
if [ ! -d "python3-virtualenv" ]; then
  echo "Error: Virtual environment folder not found."
  exit 1
fi
source python3-virtualenv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt || {
  echo "Error: Failed to install dependencies"
  exit 1
}

echo "Shut down all containers..."
docker compose -f docker-compose.prod.yml down  || {
  echo "Error: Failed to shut down containers"
  exit 1
}

echo "Re-building and starting all containers..."
docker compose -f docker-compose.prod.yml up -d --build || {
  echo "Error: Failed to build and start containers"
  exit 1
}

echo "Redeployment complete."