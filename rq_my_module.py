#!/usr/bin/env python3

import requests
from redis import Redis
from rq import Queue

# test redis queue (rq))

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

