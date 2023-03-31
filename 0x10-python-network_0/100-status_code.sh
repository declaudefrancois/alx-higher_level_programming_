#!/bin/bash
# sends a request to the URL passed as argument and display only the response code.
curl -so /dev/null "$1" -w '%{response_code}'
