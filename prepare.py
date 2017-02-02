import pandas as pd
import json
import time
import datetime

DATA_PATH = "./data/"

def get_date(row):
    start = datetime.datetime.strptime(row["Début"], "%Y-%m-%d %H:%M")
    # if he starts sleeping after midnight, the active day is just the one before
    if (start.hour >= 0 and start.hour <= 12):
        start = start - datetime.timedelta(days=1)
    return start.strftime('%Y-%m-%d')

def to_timestamp(row):
    return time.mktime(datetime.datetime.strptime(row["Date"], "%Y-%m-%d").timetuple())

# First dataset: activities.csv
data1 = pd.read_csv(DATA_PATH + "activities.csv")
data1 = data1.drop(["Dénivelé (m)", "Calories actives"], axis = 1)

# Second dataset: sleep.csv
data2 = pd.read_csv(DATA_PATH + "sleep.csv")
data2["Date"] = data2.apply(get_date, axis = 1)
data2 = data2.drop_duplicates(['Date'], keep='last') # drop naps
data2 = data2[["réveils", "Date", "profond (s)"]]

# Merge on date
data = pd.merge(data1, data2, how='inner', on='Date')
data["timestamp"] = data.apply(to_timestamp, axis = 1)
data = data.drop(["Date"], axis = 1)
data.columns = ["paces", "distance", "wakeups", "deepsleep", "timestamp"]

# Casting
data["timestamp"] = data["timestamp"].astype("int64")
data["paces"] = data["paces"].astype("int64")
data["distance"] = data["distance"].str.replace(',', '.')
data["distance"] = data["distance"].astype("float64")

# Craftai structure
context_list = []
for index, row in data.iterrows():
    context_list.append({
        "timestamp" : row["timestamp"],
        "diff" : {
            "paces" : row["paces"],                 # number of pace during the day
            "distance" : row["distance"],           # travaled distance during the day
            "deepsleep" : row["deepsleep"],         # deep sleep time during the night
        }
    })

# Output
with open(DATA_PATH + 'clean_data.json', 'w') as outfile:
    json.dump(context_list, outfile, indent = 4)
print("Saved to " + DATA_PATH + "clean_data.json")
