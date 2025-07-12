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

echo "Reloading systemd and restarting service..."
systemctl daemon-reload
systemctl restart myportfolio.service || {
  echo "Erorr: Failed to restart myportfolio.service"
  exit 1
}

echo "Redeployment complete."