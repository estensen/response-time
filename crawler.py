import requests

url = 'http://nrk.no'
r = requests.get(url)
print(r.status_code)

