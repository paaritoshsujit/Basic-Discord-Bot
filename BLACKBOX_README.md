# Discord Bot

This is a simple Discord bot that can be used to send messages to users and respond to commands. The bot is written in Python and uses the Discord.py library.

## Prerequisites

To run this bot, you will need the following:

- Python 3.6 or later
- The Discord.py library
- A Discord server

## Installation

To install the bot, clone the repository and install the requirements.

```
git clone https://github.com/paaritoshsujit/discord-bot.git
cd discord-bot
pip install -r requirements.txt
```

## Configuration

To configure the bot, you will need to create a `.env` file in the root directory of the project. The `.env` file should contain the following information:

```
DISCORD_TOKEN=your-discord-token
```

You can get your Discord token by going to the [Discord Developer Portal](https://discord.com/developers/applications).

## Running the bot

To run the bot, simply run the `main.py` file.

```
python main.py
```

The bot will then start running and will listen for messages from users.

## Usage

To use the bot, simply send a message to the bot with the following syntax:

```
?command
```

Where `command` is one of the following:

- `hello`: The bot will respond with a greeting.
- `roll`: The bot will roll a random number between 1 and 6.
- `!help`: The bot will send a help message.

## Contributing

If you would like to contribute to this project, please feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT license.
