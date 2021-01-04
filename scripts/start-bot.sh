#!/bin/bash
cd
nohup sudo -n PYTHONUNBUFFERED=1 PIPENV_DOTENV_LOCATION=.bot-secrets pipenv run python3.7 bot.py 1>~/logs/discord-bot-out.txt 2>~/logs/discord-bot-err.txt &
