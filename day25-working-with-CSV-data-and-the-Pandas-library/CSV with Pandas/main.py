
#
# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for column in data:
#         if column[1] != "temp":
#             temperatures.append(int(column[1]))
#     print(temperatures)

import pandas

#DataFrame vs Data Series#

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

#Converting Data type#

data_dictionary = data.to_dict()
# print(data_dictionary)

#Computations with pandas#

temp_list = data ["temp"].to_list()
# print(temp_list)
# print(data["temp"].median())
# print(data["temp"].max())

#Accessing Row VS Column#
#  Column  # First row will always be converted as the column of which is being referenced
print(data["condition"])#<---Can be selected as a string "Dictionary"
print(data.condition)#<---  OR as an attribute. "Object"

#  Rows  #

print(data[data.day == "Monday"])# <--- Calls a specific row by sting name that leads the row.
print(data[data.temp == data.temp.max()])# <--- Calls the max temp data row

monday = data[data.day == "Monday"]
faren = (monday.temp * 9/5) + 32
print(faren)

##  Create a DataFrame from scratch  ##

data_dict = {
    "students": ["Curto", "Christian", "James", "Chet"],
    "scores": [67, 100, 74, 70]
}
new_data = pandas.DataFrame(data_dict)
print(new_data)