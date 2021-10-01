import requests
import re

url_to_scan = "http://ya.ru"
http_page = requests.get(url_to_scan)


def links_check(some_http_page):
    pattern = r'\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]'
    for link in re.finditer(pattern, some_http_page):
        try:
            requests.head(link.group()).raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"{http_err}")
        else:
            print(f"{link.group()} - OK")


links_check(http_page.text)
