import json
import time
import datetime
import pyupbit
import discord
from discord.ext import commands
# 분할 모듈
import KeyModule
import UpbitModule
import MsgDiscord
import FileControl


# init
upbit = KeyModule.get_upbit_key()
settingJson = FileControl.open_json_file("json/upbit_setting.json")
helpJson = FileControl.open_json_file("json/help.json")

app = commands.Bot(command_prefix='$')


@app.event
async def on_ready():
    print(app.user.name, " - 디스코드 온라인.")
    await app.change_presence(status=discord.Status.online, activity=discord.Game(name="$help로 도움말 열기"))


@app.event
async def on_message(message):
    if message.author == app.user: 
        return
    if message.content.startswith('$도움말') or message.content.startswith('$help'): 
        await message.channel.send(embed=MsgDiscord.get_help_embed(helpJson["help"]))
    if message.content.startswith('$공통설정'):
        await message.channel.send(embed=MsgDiscord.get_common_setting(settingJson))
    if message.content.startswith('$위험방지'):
        await message.channel.send(embed=MsgDiscord.get_risk_block_setting(settingJson))
    if message.content.startswith('$골든크로스'):
        await message.channel.send(embed=MsgDiscord.get_golden_cross_setting(settingJson))
    if message.content.startswith('$코인동향'):
        await message.channel.send(embed=MsgDiscord.get_trend_setting(settingJson))




app.run(KeyModule.get_discord_key())