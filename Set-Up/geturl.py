import requests
import json
#from urllib.parse import urlparse
import urllib.parse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='url')
args = parser.parse_args()

#o = urlparse(args.url)
#cl =o.quote(o)

clean_url = urllib.parse.quote(args.url)
clean_url = clean_url.replace("\"","")
url = "https://tinyurl2.azurewebsites.net/api/TinyUrl?url={}".format(clean_url)
print(url)

resp = requests.post(url)
tiny_url = resp.text
print(tiny_url)
print("Run on Raspberry Pi Device:")
print("\" sudo curl -L {} | bash \"".format(tiny_url))