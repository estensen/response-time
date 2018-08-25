import concurrent.futures
import requests


def print_status(url):
    r = requests.get(url)
    print(r.status_code)


urls = [
    'https://nrk.no',
    'https://ntnu.no',
    'https://vg.no'
]


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(print_status, urls)

