#!/bin/bash
# sends a request to the URL passed as argument.
curl -so /dev/null "$1" -w '%{size_download}'; echo ""
