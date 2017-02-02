from craftai import client as craftai
from env import *
import pandas as pd
import json

DATA_PATH = "./data/"

## 1) Connect to craftai api
config = {
    "owner": CRAFT_TOKEN,
    "token": CRAFT_OWNER,
}
client = craftai.CraftAIClient(config)

## 2) Create the agent
agent_id = "Paces"
configuration = {
    "context": {
        "paces": {
            "type": 'continuous'
        },
        "distance": {
            "type": 'continuous'
        },
        "deepsleep": {
            "type": 'continuous'
        }
    },
    "output": ['deepsleep']
}

# Delet older version of the agent
client.delete_agent(agent_id)
print("Agent", agent_id, "no longer exists")

# Add the new agent
agent = client.create_agent(configuration, agent_id)
print("Agent", agent["id"], "has successfully been created")

## 3) Load and send the historical data
context_list = []
with open(DATA_PATH + 'clean_data.json') as data_file:
    context_list = json.load(data_file)

client.add_operations(agent_id, context_list)
print("List of contexts added")

## 4) Retreive the decison tree
dt_timestamp = 1477000800 # computed tree from the 2016-10-21 (example)
decision_tree = client.get_decision_tree(agent_id, dt_timestamp)

## 5) Compute a decision based on a context
context = { "paces" : 10000, "distance" : 2156 }
resp = client.decide(decision_tree, context)
print("The anticipated deep sleep time is:", resp["decision"]["deepsleep"], "seconds")
