import discord
from discord.ext import commands


def get_help_embed():
    helpEmbed = discord.Embed(title='비트코인 봇',description='업비트 연동 파이썬 비트코인 자동화 봇', color = 0x00ff00)
    helpEmbed.add_field(name='$help,$도움말',value='도움이 필요하면 불러봐요',inline=True)
    helpEmbed.add_field(name='다른 기능들',value='현재 개발중 입니다.',inline=True)
    helpEmbed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png')
    helpEmbed.set_footer(text='개발자 실버메탈',icon_url='https://blogfiles.pstatic.net/MjAyMTAxMTFfNjgg/MDAxNjEwMzQ0NTcyNTc5.Jm5ojR69wcDXz-5Q7TxN9E-WgurwADgVQqHV7_FlRlUg.Qxupnqx2LsLJCrNXnVDs04ly748VYwwpofd9HrLwwVkg.PNG.silver_metal/SMFM.png')
    return helpEmbed


def get_common_setting(setting):
    settingBoard = discord.Embed(title='현재설정',description='현재 설정된 내용')
    settingBoard.add_field(name="동작여부", value=setting["power"], inline=False)
    settingBoard.add_field(name="공통 타이밍 여부", value=setting["is_all_timing"])
    settingBoard.add_field(name="공통 타이밍 시간", value=setting["all_timing"])
    settingBoard.add_field(name="로그 표시여부", value=setting["log"], inline=False)
    return settingBoard


def get_risk_block_setting(setting):
    settingBoard = discord.Embed(title='위험방지',description='위험방지 설정된 내용')
    # for
    settingBoard.add_field(name="퍼센트", value='')
    settingBoard.add_field(name="타입", value='')
    settingBoard.add_field(name="타이밍", value='')
    settingBoard.add_field(name="이름", value='')
    return settingBoard


def get_golden_cross_setting(setting):
    settingBoard = discord.Embed(title='골든크로스',description='골든크로스 설정된 내용')
    # for
    settingBoard.add_field(name="코인", value='')
    settingBoard.add_field(name="MA", value='')
    settingBoard.add_field(name="타이밍", value='')
    return settingBoard


def get_trend_setting(setting):
    settingBoard = discord.Embed(title='코인동향',description='코인동향 설정된 내용')
    # for
    settingBoard.add_field(name="코인", value='')
    settingBoard.add_field(name="수치", value='')
    settingBoard.add_field(name="타이밍", value='')
    return settingBoard