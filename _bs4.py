#!/bin/python3

import requests

from bs4 import BeautifulSoup

letter = "S"
# url = input()
url = "http://web.archive.org/web/20201201053628/https://www.who.int/health-topics"


def gen_S(a):
    while True:
        a = a.find_next()
        if a.attrs.get("href"):
            yield a.text
        if a.text == "Sustainable Development Goals":
            break


res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

a = soup.find("a", text="Schistosomiasis")
res = [item for item in gen_S(a) if a]
print(res)
