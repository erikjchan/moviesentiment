import json

movie_dict = json.load(open('scrapers/movies.json'))

# 268896: Pacific Rim: Uprising
movie_dict["268896"]["rt_score"] = 43
movie_dict["268896"]["projected_opening"] = 25000000
movie_dict["268896"]["projected_total"] = 61000000

# 284054: Black Panther
movie_dict["284054"]["rt_score"] = 96
movie_dict["284054"]["projected_opening"] = 140000000
movie_dict["284054"]["projected_total"] = 400000000

# 299536: Avengers: Infinity War
movie_dict["299536"]["rt_score"] = 84
movie_dict["299536"]["projected_opening"] = 235000000
movie_dict["299536"]["projected_total"] = 600000000

# 333339: Ready Player One
movie_dict["333339"]["rt_score"] = 74
movie_dict["333339"]["projected_opening"] = 37000000
movie_dict["333339"]["projected_total"] = 120000000

# 370567: Sherlock Gnomes
movie_dict["370567"]["rt_score"] = 23
movie_dict["370567"]["projected_opening"] = 16000000
movie_dict["370567"]["projected_total"] = 58000000

# 419478: Midnight Sun
movie_dict["419478"]["rt_score"] = 17
movie_dict["419478"]["projected_opening"] = 3750000
movie_dict["419478"]["projected_total"] = 9400000

# 427641: Rampage
movie_dict["427641"]["rt_score"] = 51
movie_dict["427641"]["projected_opening"] = 37000000
movie_dict["427641"]["projected_total"] = 85000000

# 432301: Chappaquiddick
movie_dict["432301"]["rt_score"] = 79
movie_dict["432301"]["projected_opening"] = 3500000
movie_dict["432301"]["projected_total"] = 7000000

# 437557: Blockers
movie_dict["437557"]["rt_score"] = 83
movie_dict["437557"]["projected_opening"] = 16000000
movie_dict["437557"]["projected_total"] = 54000000

# 447332: A Quiet Place
movie_dict["447332"]["rt_score"] = 95
movie_dict["447332"]["projected_opening"] = 27500000
movie_dict["447332"]["projected_total"] = 81000000

# 454619: Overboard
movie_dict["454619"]["rt_score"] = 30
movie_dict["454619"]["projected_opening"] = 14000000
movie_dict["454619"]["projected_total"] = 39000000

# 460019: Truth or Dare
movie_dict["460019"]["rt_score"] = 14
movie_dict["460019"]["projected_opening"] = 14000000
movie_dict["460019"]["projected_total"] = 28000000

# 460668: I Feel Pretty
movie_dict["460668"]["rt_score"] = 33
movie_dict["460668"]["projected_opening"] = 17000000
movie_dict["460668"]["projected_total"] = 57000000

############################################################

# Upcoming
# 260513: Incredibles 2
movie_dict["260513"]["rt_score"] = None
movie_dict["260513"]["projected_opening"] = 110000000
movie_dict["260513"]["projected_total"] = 395000000

# 348350: Solo: A Star Wars Story
movie_dict["348350"]["rt_score"] = None
movie_dict["348350"]["projected_opening"] = 142000000
movie_dict["348350"]["projected_total"] = 390000000

# 351286: Jurassic World: Fallen Kingdom
movie_dict["351286"]["rt_score"] = None
movie_dict["351286"]["projected_opening"] = 135000000
movie_dict["351286"]["projected_total"] = 340000000

# 383498: Deadpool 2
movie_dict["383498"]["rt_score"] = None
movie_dict["383498"]["projected_opening"] = 130000000	
movie_dict["383498"]["projected_total"] = 312000000	

# 399796: Life of the Party
movie_dict["399796"]["rt_score"] = 38
movie_dict["399796"]["projected_opening"] = 21000000
movie_dict["399796"]["projected_total"] = 54000000

# 400535: Sicario: Day of the Soldado
movie_dict["400535"]["rt_score"] = None
movie_dict["400535"]["projected_opening"] = 15000000
movie_dict["400535"]["projected_total"] = 39000000

# 402900: Ocean's 8
movie_dict["402900"]["rt_score"] = None
movie_dict["402900"]["projected_opening"] = 42000000
movie_dict["402900"]["projected_total"] = 145000000

# 425148: Show Dogs
movie_dict["425148"]["rt_score"] = None
movie_dict["425148"]["projected_opening"] = 8000000
movie_dict["425148"]["projected_total"] = 25000000

# 429300: Adrift
movie_dict["429300"]["rt_score"] = None
movie_dict["429300"]["projected_opening"] = 10000000
movie_dict["429300"]["projected_total"] = 34000000

# 454283: Action Point
movie_dict["454283"]["rt_score"] = None
movie_dict["454283"]["projected_opening"] = 17000000
movie_dict["454283"]["projected_total"] = 42500000

# 455980: Tag
movie_dict["455980"]["rt_score"] = None
movie_dict["455980"]["projected_opening"] = 13000000
movie_dict["455980"]["projected_total"] = 43000000

# 474335: Uncle Drew
movie_dict["474335"]["rt_score"] = None
movie_dict["474335"]["projected_opening"] = 16500000
movie_dict["474335"]["projected_total"] = 45000000

# 497814: Breaking In
movie_dict["497814"]["rt_score"] = 34
movie_dict["497814"]["projected_opening"] = 13000000
movie_dict["497814"]["projected_total"] = 31000000

# 502682: Book Club
movie_dict["502682"]["rt_score"] = None
movie_dict["502682"]["projected_opening"] = 9500000
movie_dict["502682"]["projected_total"] = 30000000

with open('scrapers/movies.json', 'w') as outfile:
    json.dump(movie_dict, outfile, sort_keys=True, indent=4)
