#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response

# check if a URL is provided as an argument
if [[ $# -eq 0 ]]; then
  echo "Usage: $0 <url>"
  exit 1
fi

# make the curl request and get the size of the response body in bytes
response=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# display the size of the response body in bytes
echo "Size of response body: $response bytes"
