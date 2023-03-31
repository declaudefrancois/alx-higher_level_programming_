#!/bin/bash
# Send a request with a custom header and disply the response.
curl -s -H 'X-School-User-Id: 98' "$1"
