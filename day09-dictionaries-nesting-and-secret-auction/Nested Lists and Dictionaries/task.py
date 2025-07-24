capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested List in Dictionary

# travel_log = {
#     "France": ["paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

#Print Lille

# print(travel_log["France"][1])

#Nested list : print "D"
              #0    #1       #2
# nested_list = ["A", "B", ["C", "D"]]
                          #0    #1
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][2])