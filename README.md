# **craft ai** Python starter kit #

[![Build](https://img.shields.io/travis/craft-ai/craft-ai-starterkit-python/master.svg?style=flat-square)](https://travis-ci.org/craft-ai/craft-ai-starterkit-python) [![License](https://img.shields.io/badge/license-BSD--3--Clause-42358A.svg?style=flat-square)](LICENSE)

[**craft ai** _AI-as-a-service_](http://craft.ai) enables developers to create Apps and Things that adapt to each user. To go beyond useless dashboards and spammy notifications, **craft ai** learns how users behave to automate recurring tasks, make personalized recommendations, or detect anomalies.

This repository hosts a fully working application, in a **Personal Wellness Analysis** context, integrating [**craft ai**](http://craft.ai) written in Python using [**craft ai** official Python client](https://pypi.python.org/pypi?:action=display&name=craft-ai).

The end goal: improve the _sleep_ of the user based on its _historical sleep data_. We have several days data containing _details_ about his day and the time he slept consequently after this day during the night. Using **craft ai**, this simple application learns how well the user can sleep regarding to his day data. We want to inform the user how well he may sleep at night regarding to how he used to sleep after a similar day.

## Setup ##

- Download or clone the [sources from GitHub](https://github.com/craft-ai/craft-ai-starterkit-python),
- Install [Python](https://www.python.org/downloads/) on your computer (version >=3.5 is recommended),
- Install the **craft ai** python client using `pip` by running `pip install --upgrade craft-ai` in a terminal.
- in this directory, fill the `env.py` file setting the following variables:
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

Now that you know how to compute your decision tree, you are able to complete the initial goal: predict the user's **sleep time**.

You can add context operations in real time, day after day, and compute a decision when the context changes that can be used, in conjuction with its confidence, to encourage the user to go to bed at a certain hour in order to have the best night possible.

## About the dataset ##

This starter kit uses real data anonymized and extracted from a personal connected watch owned by a **craft ai** team member. The data is stored in `sleep_data.csv`. Each line corresponds to the day details and the following night sleep. The features are:

* `date` the date of the day
* `day_off` day is off or not
* `next_day_off` sleep at home or not
* `sleep_at_home` sleep at home or not
* `sleep_start` hour at which he started to sleep
* `timezone` timezone for `sleep_start` hour
* `sleep` sleep time during the night

### Data preparation ###

> The pre-treated data are already computed and available for this example.

The data can be treated and then output by the script `prepare.py`. The cleaned data is already provided in the `data` folder but you can output it again by running:
```console
python prepare.py
```

The result will be set in `data/clean_data.json`.

You can check out `prepare.py` to see what we've done and make your own preparation.

> The **craft ai** user documentation can be found at <https://beta.craft.ai/doc> and technical questions can be sent by email at [support@craft.ai]('mailto:support@craft.ai').
