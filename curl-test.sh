#!/bin/bash

# Base URL of your Flask server (adjust if needed)
BASE_URL="http://127.0.0.1:5000/api/timeline_post"

# Generate random values
NAME="TestUser_$RANDOM"
EMAIL="testuser_$RANDOM@example.com"
CONTENT="This is a test post at $(date)."

echo "Posting a new timeline post..."
POST_RESPONSE=$(curl -X POST "$BASE_URL" \
  -d "name=$NAME" \
  -d "email=$EMAIL" \
  -d "content=$CONTENT")

echo "POST Response:"
echo "$POST_RESPONSE"

# Extract the returned ID using jq or grep+sed
POST_ID=$(echo "$POST_RESPONSE" | grep -o '"id":[0-9]*' | sed 's/[^0-9]*//g')

echo "\nVerifying with GET request..."
curl "$BASE_URL" | grep "$CONTENT" && echo "Post found in GET response!" || echo "Post not found."


if [[ "$POST_ID" != "" ]]; then
  echo "\n🗑️ Deleting test post ID $POST_ID..."
  curl -X DELETE "$BASE_URL/$POST_ID"
  echo  "Post deleted."
else
  echo "Could not extract post ID. Skipping delete."
fi