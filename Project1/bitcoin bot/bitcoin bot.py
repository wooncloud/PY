import os
import json
import time
import datetime
import pyupbit
import discord
from discord.ext import commands
# 분할 모듈
import KeyModule
import MsgDiscord
import FileControl


# init
upbit = KeyModule.get_upbit_key()
settingJson = FileControl.open_json_file("upbit_setting.json")

app = commands.Bot(command_prefix='$')


@app.event
async def on_ready():
    print(app.user.name, " - 디스코드 온라인.")
    await app.change_presence(status=discord.Status.online, activity=discord.Game(name="$help로 도움말 열기"))


@app.event
async def on_message(message):
    tempEmbed = None

    if message.author == app.user: 
        return
    if message.content.startswith('$도움말') or message.content.startswith('$help'): 
        helpEmbed = MsgDiscord.get_help_embed()
        await message.channel.send(embed=helpEmbed)
    if message.content.startswith('$공통설정'):
        tempEmbed = MsgDiscord.get_common_setting(settingJson)
        await message.channel.send(embed=tempEmbed)
    if message.content.startswith('$위험방지'):
        tempEmbed = MsgDiscord.get_risk_block_setting(settingJson)
        await message.channel.send(embed=tempEmbed)
    if message.content.startswith('$골든크로스'):
        tempEmbed = MsgDiscord.get_golden_cross_setting(settingJson)
        await message.channel.send(embed=tempEmbed)
    if message.content.startswith('$코인동향'):
        tempEmbed = MsgDiscord.get_trend_setting(settingJson)
        await message.channel.send(embed=tempEmbed)

    tempEmbed = None


app.run(KeyModule.get_discord_key())