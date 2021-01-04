#!/bin/bash
cd
nohup sudo -b PIPENV_DOTENV_LOCATION=.bot-secrets pipenv run python3.7 bot.py
