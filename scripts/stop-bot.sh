#!/bin/bash
ps -ax | grep bot.py | grep -v grep > ~/processes.txt
ps -ax | grep bot.py | grep -v grep | awk '{print $1}' | xargs sudo kill
