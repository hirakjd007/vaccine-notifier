# vaccine-notifier

## Introduction

This Python script will poll the CoWin public APIs to check for slots based on the interval defined in the script. Once a slot with the defined filters is available it will send a notification to telegram user/channel/bot ( as defined by users)

## Installation

### Note: This library requires Python 3.6+ and a Telegram BOT to send messages to telegram user/channel

1. Install Python  See [Python documentation](https://www.python.org/downloads/) for more details on how to install Python .

1. Create a telegram bot. See [Telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot) for more details on Telegram BOT. You will receive a bot token (eg. 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw)

    **Note: The token is a string along the lines of 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw that is required to             authorize   the bot and send requests to the Bot API. Keep your token secure and store it safely, it can be used by anyone     to control your bot.**

1. Create a new channel/group or an existing group where you want to send notifications. Make the BOT (you have created above) as an admin.

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
|**`my_token`**|string|TELEGRAM BOT Token with prefix as **bot**|true
|**`chat_id`**|string|Chat ID for user,bot OR @channel-name|true
|**`min_age_limit`**|number|Minimum Age Group|true
|**`vaccine`**|string|Vaccine Preference i.e COVISHILED or COVAXIN|true
|**`fee_type`**|string|Free type i.e Free or Paid|true

1. Run the script using 

```shell
cd vaccine-notifier
python covaccinate.py
```
Once a slot is available, you will be notified in the your channel
----

## Development

See [CONTRIBUTING.md](/CONTRIBUTING.md).
