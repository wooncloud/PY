import os
import time
import datetime
import pyupbit
import discord
from discord.ext import commands
# 분할 모듈
import KeyModule
import MsgDiscord


# init
upbit = KeyModule.get_upbit_key()
MsgDiscord.app.run(KeyModule.get_discord_key())