#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response.
curl -LsIi 0.0.0.0:5000 | grep -iF "content-length" | awk -F" " '{print $2}'
