import json
reverse_keywords_dict = json.load(open('scrapers/reverse_keywords.json'))

TRACK_TERMS = list(reverse_keywords_dict.keys())

TABLE_NAME = "movie"

try:
    from private import *
except Exception:
    pass