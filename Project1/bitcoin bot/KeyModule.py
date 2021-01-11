import os
import pyupbit

def get_discord_key():
    path = os.getcwd() + "/.key/discord bot token.txt"
    token = None
    with open(path) as f:
        lines = f.readlines()
        token = lines[0].strip()

    return token


def get_upbit_key():
    path = os.getcwd() + "/.key/upbit key.txt"
    key = None
    secret = None

    with open(path) as f:
        lines = f.readlines()
        key = lines[0].strip()
        secret = lines[1].strip()
        
    return pyupbit.Upbit(key, secret)