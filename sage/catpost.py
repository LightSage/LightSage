"""Cat post!"""
import requests


def get_from_catapi(limit=1):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    r = r.json()
    return r[0]
