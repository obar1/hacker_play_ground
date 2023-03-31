#!/bin/python3

import requests


class InvalidQuoteResource(Exception):
    def __init__(self, message="Invalid quote resource!"):
        self.message = message
        super().__init__(self.message)


class InvalidPage(Exception):
    def __init__(self, message="Invalid page!"):
        self.message = message
        super().__init__(self.message)


def get_soup(res):
    from bs4 import BeautifulSoup

    return BeautifulSoup(res.content, "html.parser")


def get_title(soup):
    return {"title": soup.find("title").text}


def get_description(soup):
    description = soup.find("head").find_all("meta", {"name": "description"})[0]
    return {"description": description.attrs["content"]}


def invoke_http(url):
    response = requests.get(url=url, headers={"Accept-Language": "en-US,en;q=0.5"})
    if "nature.com" not in url:
        raise InvalidPage()

    if response.status_code != 200:
        raise InvalidQuoteResource()
    soup = get_soup(response)
    print(get_title(soup) | get_description(soup))


if __name__ == "__main__":
    url = input()
    #     url = 'https://www.nature.com/articles/d41586-023-00103-3'
    try:
        res = invoke_http(url)
        print(res)
    except Exception as e:
        print(e)
