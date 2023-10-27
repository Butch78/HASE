#!/bin/bash

# Test the root endpoint
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/)
if [ "$response" -ne 200 ]; then
    echo "Root endpoint test failed with status $response"
else
    echo "Root endpoint test passed"
fi

# Test the /items/{item_id} endpoint
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/items/1?q=test)
if [ "$response" -ne 200 ]; then
    echo "/items/{item_id} endpoint test failed with status $response"
else
    echo "/items/{item_id} endpoint test passed"
fi