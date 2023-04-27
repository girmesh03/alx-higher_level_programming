#!/bin/bash
# A Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!.
curl -sLX PUT -d "user_id=98" 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"
