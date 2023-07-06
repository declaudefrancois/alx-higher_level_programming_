#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response.
curl -Lso /dev/null -w "%{size_download}"  0.0.0.0:5000 && echo
