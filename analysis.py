import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read in all the data from csvs. These are exactly what TomTom provided me.
data_2019 = pd.read_csv("data-2019.csv")
data_2020 = pd.read_csv("data-2020.csv")
data_2021 = pd.read_csv("data-2021.csv")
data_2021_2 = pd.read_csv("data-2021.csv")

# Put them all together into one dataframe.
data = pd.concat([data_2019, data_2020, data_2021])

# Include only the columns I'm interested in.
data = pd.DataFrame(data[["Date", "Hour", "Live Congestion Level [%]"]])

# Two new columns for year and day.
data["year"] = data["Date"].str.slice(start=0, stop=4)
data["day"] = data["Date"].str.slice(start=5)

# Export
data.to_csv("data-all.csv")
print(data)

# Daily change pivot.
pivot = pd.pivot_table(data, columns="year", index="day", values="Live Congestion Level [%]", aggfunc='mean')

# Calculate change columns.
pivot["change (2019-2020)"] = pivot["2020"] - pivot["2019"]
pivot["change (2020-2021)"] = pivot["2021"] - pivot["2020"]

# Export
pivot.to_csv("date-comparison.csv")
print(pivot)