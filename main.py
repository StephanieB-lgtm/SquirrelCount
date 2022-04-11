
import pandas
data = pandas.read_csv("2018_Squirrel_data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
red_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])

print(f"{gray_color_count} gray squirrel")
print(f"{red_color_count} red squirrel")
print(f"{black_color_count} black squirrel")


data_dict={
    "Fur Color" : ["Gray", "Cinnamon", "Black",],
    "Count": [gray_color_count, red_color_count, black_color_count]
}
df= pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
