# **craft ai** Python starter kit #

[![Build](https://img.shields.io/travis/craft-ai/craft-ai-starterkit-python/master.svg?style=flat-square)](https://travis-ci.org/craft-ai/craft-ai-starterkit-python) [![License](https://img.shields.io/badge/license-BSD--3--Clause-42358A.svg?style=flat-square)](LICENSE)

[**craft ai** _AI-as-a-service_](http://craft.ai) enables developers to create Apps and Things that adapt to each user. To go beyond useless dashboards and spammy notifications, **craft ai** learns how users behave to automate recurring tasks, make personalized recommendations, or detect anomalies.

This repository hosts a fully working application, in a **Personal Health Analysis** context, integrating [**craft ai**](http://craft.ai) written in Python using [**craft ai** official Python client](https://pypi.python.org/pypi?:action=display&name=craft-ai).

The end goal: improve the _deep sleep_ time of the user based on its _number of pace_ and _travaled distance_ during the day. Using **craft ai**, this simple application learns how well the user can sleep regarding to its day activity, measured by a connected object such as a watch.

## Setup ##

- Download or clone the [sources from GitHub](https://github.com/craft-ai/craft-ai-starterkit-python),
- Install [Python](https://www.python.org/downloads/) on your computer (version >=3.5 is recommended),
- Install the **craft ai** python client using `pip` by running `pip install --upgrade craft-ai` in a terminal.
- in this directory, create a `.env` file setting the following variables:
    - `CRAFT_TOKEN` allows you to [authenticate your calls to the **craft ai** API](https://beta.craft.ai/doc/python#1---retrieve-your-credentials),
    - `CRAFT_OWNER` define the **owner** of the craft ai agents that will be created

## Run ##

The following will:

1. create an agent,
2. add a bunch of context operations from the example dataset,
3. compute a decision tree and
4. take a few decisions.

```console
python main.py
```

### What do next ? ###

Now that you know how to compute your decision tree, you are able to complete the initial goal: predict the user's sleep quality.

You can use the devices input to add context operations in real time and compute a decision when the context changes that can be used, in conjuction with its confidence, to encourage the user to move more or not.

## About the dataset ##

This starter kit uses real data anonymized and extracted from a personal connected watch owned by a **craft ai** team member.

### Data preparation ###

> The pre-treated data are already computed and available for this example.

We only use the paces done and the distance traveled during the day before the predicted night, because they are the cleanest and more relevant features from our dataset.
For that, we merge on the date the two original datasets: `activities.csv` and `sleep.csv`.

The data is treated and then output by the script `prepare.py`. The cleaned data is already provided in the `data` folder but you can output it again by running:
```console
python prepare.py
```

The result will be set in `data/clean_data.json`.

You can check out `prepare.py` to see what we've done and make your own preparation.

> The **craft ai** user documentation can be found at <https://beta.craft.ai/doc> and technical questions can be sent by email at [support@craft.ai]('mailto:support@craft.ai').
