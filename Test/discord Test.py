import os
import discord
from discord.ext import commands

app = commands.Bot(command_prefix='$')


def get_key():
    path = os.getcwd() + "/.key/discord bot token.txt"
    token = None
    with open(path) as f:
        lines = f.readlines()
        token = lines[0].strip()

    return token


def set_embed():
    embed = discord.Embed(title='비트코인 봇',description='업비트 연동 파이썬 비트코인 자동화 봇', color = 0x00ff00)
    embed.add_field(name='$help,$도움말',value='도움이 필요하면 불러봐요',inline=True)
    embed.add_field(name='다른 기능들',value='현재 개발중 입니다.',inline=True)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png')
    embed.set_footer(text='개발자 실버메탈',icon_url='https://blogfiles.pstatic.net/MjAyMTAxMTFfNjgg/MDAxNjEwMzQ0NTcyNTc5.Jm5ojR69wcDXz-5Q7TxN9E-WgurwADgVQqHV7_FlRlUg.Qxupnqx2LsLJCrNXnVDs04ly748VYwwpofd9HrLwwVkg.PNG.silver_metal/SMFM.png')

    return embed


helpEmbed = set_embed()


@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)


@app.event
async def on_message(message):
    if message.author == app.user: 
        return
    if message.content.startswith('$도움말') or message.content.startswith('$help'): 
        await message.channel.send(embed=helpEmbed)


# 시작
app.run(get_key())
