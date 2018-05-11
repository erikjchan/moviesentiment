import json

keywords_dict = dict()

keywords_dict[268896] = ["pacific rim: uprising", "pacific rim uprising", "pacificrimuprising", "pacificrimmovie"]
keywords_dict[284054] = ["black panther", "blackpanther"]
keywords_dict[299536] = ["infinity war", "infinitywar"]
keywords_dict[333339] = ["ready player one", "readyplayerone"]
keywords_dict[370567] = ["sherlock gnomes", "sherlockgnomes"]
keywords_dict[419478] = ["midnight sun", "midnightsunmovie", "midnightsun_mov"]
keywords_dict[427641] = ["rampagemovie", "rampage movie", "rampagethemovie"]
keywords_dict[432301] = ["chappaquiddick"]
keywords_dict[437557] = ["blockersmovie", "blockers movie"]
keywords_dict[447332] = ["a quiet place", "quietplacemovie", "quiet place movie", "aquietplace"]
keywords_dict[454619] = ["overboardmovie", "overboard movie"]
keywords_dict[460019] = ["truthdaremovie", "truthordaremovie", "truth or dare movie", "blumhouse's truth or dare"]
keywords_dict[460668] = ["i feel pretty movie", "#ifeelpretty"]

# Upcoming
keywords_dict[260513] = ["incredibles 2", "incredibles2", "incredibles sequel"]
keywords_dict[348350] = ["solo: a star wars story", "solo a star wars story", "soloastarwarsstory", "#solo"]
keywords_dict[351286] = ["jurassic world: fallen kingdom", "jurassic world fallen kingdom", "jurassic world 2", "jurassic world sequel", "fallenkingdom"]
keywords_dict[383498] = ["deadpool 2", "deadpool2", "deadpool sequel"]
keywords_dict[399796] = ["life of the party movie", "lifeoftheparty" "lotpmovie"]
keywords_dict[400535] = ["sicario: day of the soldado", "sicario day of the soldado", "sicariodayofthesoldado", "sicario 2", "sicario sequel", "sicariomovie"]
keywords_dict[402900] = ["ocean's 8", "oceans8", "ocean's eight", "oceanseight"]
keywords_dict[425148] = ["show dogs movie", "showdogsmovie", "showdogsmov"]
keywords_dict[429300] = ["adrift movie", "adriftmovie"]
keywords_dict[454283] = ["action point movie", "actionpointmov", "actionpoint"]
keywords_dict[455980] = ["tagthemovie", "tagmovie"]
keywords_dict[474335] = ["uncle drew movie", "uncledrewfilm", "uncledrew"]
keywords_dict[497814] = ["breaking in movie", "breakinginmovie"]
keywords_dict[502682] = ["book club movie", "bookclubmovie"]

reverse_keywords_dict = dict()
for k, v in keywords_dict.iteritems():
	for x in v:
		reverse_keywords_dict[x] = k


with open('scrapers/keywords.json', 'w') as outfile:
    json.dump(keywords_dict, outfile, sort_keys=True, indent=4)

with open('scrapers/reverse_keywords.json', 'w') as outfile:
    json.dump(reverse_keywords_dict, outfile, sort_keys=True, indent=4)
