# #100days of code - day 25 - Exercises

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
#     for x in range(0, len(data)):
#         data[x] = data[x].strip()
#
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         # print(row[1])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")  # don't need to open file
# #print(data)
# #print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
# # average temp without pandas
# temp_list = data["temp"].to_list()
# print(temp_list)
# avg = sum(temp_list) / len(temp_list)
# print(avg)
#
# # average temp using pandas
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
#
# # data from rows
# print(data[data.day == "Monday"])
#
# # row with max temp
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# # monday_temp_F = (monday.temp * 9/5) + 32
# monday_temp_F = (int(monday.temp) * 9/5) + 32
# print(monday_temp_F)
#
# # create dataframe from scratch (without datafile)
# students_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# students_dataframe = pandas.DataFrame(students_dict)
# print(students_dataframe)
# # students_dataframe.to_csv("students.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(squirrel_data)
squirrel_color = squirrel_data["Primary Fur Color"]
squirrel_count = squirrel_color.value_counts()
print(squirrel_count)
squirrel_count.to_csv("squirrel_count.csv")

#another method
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count2.csv")


