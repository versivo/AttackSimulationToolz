#!/usr/bin/env python3

import requests
import sys

payload = {"domain": sys.argv[1]}

r = requests.post("https://services.blackkitetech.com/api/v1/breach/domain", json=payload)

output = r.json()

for item in output["results"]["breachList"]:
    print(item["Email"])
