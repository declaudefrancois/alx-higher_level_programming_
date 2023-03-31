#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument.
curl -Ls -X POST -H "Content-Type: application/json" -d @"$2" "$1"
