#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json

import requests


# Complete the function below.
# Base url: https://jsonmock.hackerrank.com/api/movies/search/?Title=


def get_data(movie):
    url = f"https://jsonmock.hackerrank.com/api/movies/search/?Title={movie}"
    count = 1
    while True:
        # print(count)
        data = requests.get(url + f"&page={count}")
        # print(data)
        response = json.loads(data.content.decode("utf-8"))
        # print(data.content)
        count += 1
        if len(response["data"]) == 0:
            break
        yield response["data"]


def getMovieTitles(substr):
    # print(substr)
    movies = list(get_data(substr))
    # print([*movies]) # unpacking

    titles = []
    for movie_set in range(len(movies)):
        for m in movies[movie_set]:
            # print(m)
            titles.append(str(m["Title"]))
    titles.sort()
    return titles


f = open(os.environ["OUTPUT_PATH"], "w")


try:
    _substr = str(input())
except:
    _substr = None

res = getMovieTitles(_substr)
for res_cur in res:
    f.write(str(res_cur) + "\n")

f.close()
