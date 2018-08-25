import requests

urls = [
    'https://nrk.no',
    'https://ntnu.no',
    'https://vg.no'
]

for url in urls:
    r = requests.get(url)
    print(r.status_code)

