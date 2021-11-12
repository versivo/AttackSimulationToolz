import sys
import requests
import time
import json

# vars
shodan_baseurl =    "https://api.shodan.io"
shodan_api =        "/shodan/host"
shodan_auth =       ""  # your shodan key

# get reports list
host = sys.argv[1]
url = shodan_baseurl + shodan_api + '/' + host + '?key=' + shodan_auth
print("Get data from {}".format(url))
response = requests.get(url)
data = response.json()

# select some data
print("--------------------------------------------------")
print("Region: \t{}".format(data["region_code"]))
print("Hostname(s): \t{}".format(data["hostnames"]))

# raw data
print("--------------------------------------------------")
print(data)
