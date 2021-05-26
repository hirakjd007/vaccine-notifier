# vaccine-notifier

## Introduction

This Python script will poll the CoWin public APIs to check for slots based on the interval defined in the script. Once a slot with the defined filters is available it will send a notification to telegram user/channel/bot ( as defined by users)

## Installation

This library requires Python 3.6+ and Linux or MacOS.

See [Python documentation](https://www.python.org/downloads/) for more details on how to install Python .

1. Clone this repository.

1. Install packages.

```shell
sudo install pip
python -m pip install --upgrade pip
pip install requests
```

## How to use

Basic settings and filters:


The script accepts the following config props:

|Name|Type|Description|Required
|:--:|:-----|:-----|:-----|
|**`poll_interval`**|number|Poll Interval in seconds|true
|**`my_token`**|string|TELEGRAM BOT Token|true
|**`chat_id`**|string|Chat ID for user,bot OR @channel-name|true
|**`min_age_limit`**|number|Minimum Age Group|true
|**`vaccine`**|string|Vaccine Preference i.e COVISHILED or COVAXIN|true
|**`fee_type`**|string|Free type i.e Free or Paid|true

1. Run the script using 

```shell
python covaccinate.py
```
----

## Development

See [CONTRIBUTING.md](/CONTRIBUTING.md).
