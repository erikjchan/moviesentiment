import json
now_playing_dict = json.load(open('scrapers/now_playing.json'))

# 268896: Pacific Rim: Uprising
now_playing_dict["268896"]["rt_score"] = 43
now_playing_dict["268896"]["projected_opening"] = 25000000
now_playing_dict["268896"]["projected_total"] = 61000000

# 284054: Black Panther
now_playing_dict["284054"]["rt_score"] = 96
now_playing_dict["284054"]["projected_opening"] = 140000000
now_playing_dict["284054"]["projected_total"] = 400000000

# 299536: Avengers: Infinity War
now_playing_dict["299536"]["rt_score"] = 84
now_playing_dict["299536"]["projected_opening"] = 235000000
now_playing_dict["299536"]["projected_total"] = 600000000

# 333339: Ready Player One
now_playing_dict["333339"]["rt_score"] = 74
now_playing_dict["333339"]["projected_opening"] = 37000000
now_playing_dict["333339"]["projected_total"] = 120000000

# 370567: Sherlock Gnomes
now_playing_dict["370567"]["rt_score"] = 23
now_playing_dict["370567"]["projected_opening"] = 16000000
now_playing_dict["370567"]["projected_total"] = 58000000

# 419478: Midnight Sun
now_playing_dict["419478"]["rt_score"] = 17
now_playing_dict["419478"]["projected_opening"] = 3750000
now_playing_dict["419478"]["projected_total"] = 9400000

# 427641: Rampage
now_playing_dict["427641"]["rt_score"] = 51
now_playing_dict["427641"]["projected_opening"] = 37000000
now_playing_dict["427641"]["projected_total"] = 85000000

# 432301: Chappaquiddick
now_playing_dict["432301"]["rt_score"] = 79
now_playing_dict["432301"]["projected_opening"] = 3500000
now_playing_dict["432301"]["projected_total"] = 7000000

# 437557: Blockers
now_playing_dict["437557"]["rt_score"] = 83
now_playing_dict["437557"]["projected_opening"] = 16000000
now_playing_dict["437557"]["projected_total"] = 54000000

# 447332: A Quiet Place
now_playing_dict["447332"]["rt_score"] = 95
now_playing_dict["447332"]["projected_opening"] = 27500000
now_playing_dict["447332"]["projected_total"] = 81000000

# 454619: Overboard
now_playing_dict["454619"]["rt_score"] = 30
now_playing_dict["454619"]["projected_opening"] = 14000000
now_playing_dict["454619"]["projected_total"] = 39000000

# 460019: Truth or Dare
now_playing_dict["460019"]["rt_score"] = 15
now_playing_dict["460019"]["projected_opening"] = 14000000
now_playing_dict["460019"]["projected_total"] = 28000000

# 460668: I Feel Pretty
now_playing_dict["460668"]["rt_score"] = 33
now_playing_dict["460668"]["projected_opening"] = 17000000
now_playing_dict["460668"]["projected_total"] = 57000000

with open('scrapers/now_playing.json', 'w') as outfile:
    json.dump(now_playing_dict, outfile, sort_keys=True, indent=4)

################################################################################

upcoming_dict = json.load(open('scrapers/upcoming.json'))

# Upcoming
# 260513: Incredibles 2
upcoming_dict["260513"]["rt_score"] = None
upcoming_dict["260513"]["projected_opening"] = 110000000
upcoming_dict["260513"]["projected_total"] = 395000000

# 348350: Solo: A Star Wars Story
upcoming_dict["348350"]["rt_score"] = None
upcoming_dict["348350"]["projected_opening"] = 142000000
upcoming_dict["348350"]["projected_total"] = 390000000

# 351286: Jurassic World: Fallen Kingdom
upcoming_dict["351286"]["rt_score"] = None
upcoming_dict["351286"]["projected_opening"] = 135000000
upcoming_dict["351286"]["projected_total"] = 340000000

# 383498: Deadpool 2
upcoming_dict["383498"]["rt_score"] = None
upcoming_dict["383498"]["projected_opening"] = 130000000	
upcoming_dict["383498"]["projected_total"] = 312000000	

# 399796: Life of the Party
upcoming_dict["399796"]["rt_score"] = 35
upcoming_dict["399796"]["projected_opening"] = 21000000
upcoming_dict["399796"]["projected_total"] = 54000000

# 400535: Sicario: Day of the Soldado
upcoming_dict["400535"]["rt_score"] = None
upcoming_dict["400535"]["projected_opening"] = 15000000
upcoming_dict["400535"]["projected_total"] = 39000000

# 402900: Ocean's 8
upcoming_dict["402900"]["rt_score"] = None
upcoming_dict["402900"]["projected_opening"] = 42000000
upcoming_dict["402900"]["projected_total"] = 145000000

# 425148: Show Dogs
upcoming_dict["425148"]["rt_score"] = None
upcoming_dict["425148"]["projected_opening"] = 8000000
upcoming_dict["425148"]["projected_total"] = 25000000

# 429300: Adrift
upcoming_dict["429300"]["rt_score"] = None
upcoming_dict["429300"]["projected_opening"] = 10000000
upcoming_dict["429300"]["projected_total"] = 34000000

# 454283: Action Point
upcoming_dict["454283"]["rt_score"] = None
upcoming_dict["454283"]["projected_opening"] = 17000000
upcoming_dict["454283"]["projected_total"] = 42500000

# 455980: Tag
upcoming_dict["455980"]["rt_score"] = None
upcoming_dict["455980"]["projected_opening"] = 13000000
upcoming_dict["455980"]["projected_total"] = 43000000

# 474335: Uncle Drew
upcoming_dict["474335"]["rt_score"] = None
upcoming_dict["474335"]["projected_opening"] = 16500000
upcoming_dict["474335"]["projected_total"] = 45000000

# 497814: Breaking In
upcoming_dict["497814"]["rt_score"] = 37
upcoming_dict["497814"]["projected_opening"] = 13000000
upcoming_dict["497814"]["projected_total"] = 31000000

# 502682: Book Club
upcoming_dict["502682"]["rt_score"] = None
upcoming_dict["502682"]["projected_opening"] = 9500000
upcoming_dict["502682"]["projected_total"] = 30000000

with open('scrapers/upcoming.json', 'w') as outfile:
    json.dump(upcoming_dict, outfile, sort_keys=True, indent=4)
