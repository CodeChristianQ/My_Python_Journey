#In this project the objective is to extract specific data from the Squirrel Census to then create my own csv file that
# displays the

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_squirl_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_squirl_dictionary)
df.to_csv("squirrel_count.csv")