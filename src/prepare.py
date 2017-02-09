import pandas as pd
from datetime import datetime
import json

# Load the dataset
data = pd.read_csv('../data/sleep_data.csv')

# Convert date into timestamp
data["timestamp"] = data.apply(lambda x: datetime.strptime(x['date'], '%Y-%m-%d').timestamp(), axis=1).astype('int64')

# Enum type must be string
data["day_off"] = data["day_off"].astype(str)
data["next_day_off"] = data["next_day_off"].astype(str)
data["sleep_at_home"] = data["sleep_at_home"].astype(str)

# Convert in craft ai python dictionnary structure
context_list = []
for index, row in data.iterrows():
    context_list.append({
        "timestamp" : row["timestamp"],
        "diff" : {
            "day_off" : row["day_off"],
            "next_day_off" : row["next_day_off"],
            "sleep_at_home" : row["sleep_at_home"],
            "sleep_start" : row["sleep_start"],
            "sleep" : row["sleep"],
            "timezone" : row["timezone"]
        }
    })

# Output
with open('../data/clean_data.json', 'w') as outfile:
    json.dump(context_list, outfile, indent = 3)
print("Saved to ../data/clean_data.json")
