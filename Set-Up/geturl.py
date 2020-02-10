import requests
import json
import urllib.parse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='url')
args = parser.parse_args()


headers = {'Content-Type':'application/text'}

clean_url = urllib.parse.quote(args.url)
url = "https://tinyurl2.azurewebsites.net/api/TinyUrl?url={}".format(clean_url)
url = url.replace("%22","")
print(url)

resp = requests.post(url,headers=headers)
print(resp.status_code)
tiny_url = resp.text
print(tiny_url)
print("Run on Raspberry Pi Device:")
print(" sudo curl -L {} | bash ".format(tiny_url))