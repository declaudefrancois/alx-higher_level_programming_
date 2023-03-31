#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response.
curl -s -d 'email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD' "$1"
