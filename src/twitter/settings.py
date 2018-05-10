TRACK_TERMS = ["infinity war"]
CONNECTION_STRING = "sqlite:///tweets.db"
CSV_NAME = "tweets.csv"
TABLE_NAME = "movie"

try:
    from private import *
except Exception:
    pass