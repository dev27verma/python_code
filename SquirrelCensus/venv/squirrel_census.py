import pandas

data = pandas.read_csv("census_data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
grey_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

new_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
            "Count": [gray_count,grey_count,black_count]
            }

df = pandas.DataFrame(new_dict)
df.to_csv("new_census_data.csv")