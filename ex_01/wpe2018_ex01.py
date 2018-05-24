#!/usr/bin/python3

## Ask user to enter locations they've visited
loc_info = {}

ask_again = True
while ask_again:
    city_country = input('Tell me where you went:')
    
    # Can we get out of here?
    # User must have a blank response
    if len(city_country) == 0:
        # Yes, let's bust out of here
        ask_again = False
        continue
    
    # Keep going
    # Did the user supply a comma?
    if ',' not in city_country:
        print("That's not a legal city, {}".format(city_state, ))
        continue
    
    # Wooho, a valid(ish) city,country
    # split up city and country
    city_info = city_country.split(",")

    # sanity check (make sure we have two elements)
    if len(city_info) != 2:
        print("That's not a legal city, {}".format(city_state, ))
        continue

    # keep track of cities and countries
    city, country = city_info 
    if loc_info.get(country) is None:
        loc_info[country] = []
    loc_info[country].append(city)

## Print out a summary of locations visited
print("You visited:")
for country in sorted(iter(loc_info.keys())):
    print(country)
    # get a unique list of cities
    cities = loc_info[country]
    cities_cnt = {}
    cities_uniq = []
    for city in cities:
        if city not in cities_uniq:
            cities_uniq.append(city)
            cities_cnt[city] = 0
        cities_cnt[city] += 1

    # print out summary!
    cities_uniq.sort()
    for city in cities_uniq:
        cnt = cities_cnt[city]
        print("    {} ({})".format(city, cnt, ))
