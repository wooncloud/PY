import discord
from discord.ext import commands
import KeyModule


client = discord.Client()


class DiscordBot(discord.Client):
    def get_help_embed(self, helpJson):
        helpEmbed = discord.Embed(title='비트코인 봇',description='업비트 연동 파이썬 비트코인 자동화 봇', color = 0x00ff00)
        helpEmbed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png')
        helpEmbed.set_footer(text='개발자 실버메탈',icon_url='https://blogfiles.pstatic.net/MjAyMTAxMTFfNjgg/MDAxNjEwMzQ0NTcyNTc5.Jm5ojR69wcDXz-5Q7TxN9E-WgurwADgVQqHV7_FlRlUg.Qxupnqx2LsLJCrNXnVDs04ly748VYwwpofd9HrLwwVkg.PNG.silver_metal/SMFM.png')
        for item in helpJson:
            helpEmbed.add_field(name=item["name"],value=item["value"],inline=item["inline"])
        return helpEmbed


    def get_common_setting(self, setting):
        settingBoard = discord.Embed(title='공통설정',description='현재 설정된 내용')
        settingBoard.add_field(name="동작여부", value=setting["power"], inline=False)
        settingBoard.add_field(name="공통 타이밍 여부", value=setting["is_all_timing"])
        settingBoard.add_field(name="공통 타이밍 시간", value=setting["all_timing"])
        settingBoard.add_field(name="로그 표시여부", value=setting["log"], inline=False)
        return settingBoard


    def get_risk_block_setting(self, setting):
        i = 0
        settingBoard = discord.Embed(title='위험방지',description='위험방지 설정된 내용')
        for item in setting["risk_block"]:
            i = i + 1
            itemValue = "수치 : %0.1f%% / 타입 : %s / 타이밍 : %s / 이름 : %s" % (item["value"], item["type"], item["timing"], item["name"])
            settingBoard.add_field(name=str(i), value=itemValue, inline=False)
        return settingBoard


    def get_golden_cross_setting(self, setting):
        i = 0
        settingBoard = discord.Embed(title='골든크로스',description='골든크로스 설정된 내용')
        for item in setting["golden_cross"]:
            i = i + 1
            itemValue = "코인 : %s / MA : %d / 타이밍 : %s" % (item["coin"], item["MA"], item["timing"])
            settingBoard.add_field(name=str(i), value=itemValue, inline=False)
        return settingBoard


    def get_trend_setting(self, setting):
        i = 0
        settingBoard = discord.Embed(title='코인동향',description='코인동향 설정된 내용')
        for item in setting["trend"]:
            i = i + 1
            itemValue = "코인 : %s / 수치 : %0.1f%% / 타이밍 : %s" % (item["coin"], item["value"], item["timing"])
            settingBoard.add_field(name=str(i), value=itemValue, inline=False)
        return settingBoard


    async def on_ready(self):
        print(client.user.name, " - 디스코드 온라인.")
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name="$help로 도움말 열기"))


    async def on_message(self, message):
        if message.author == client.user: 
            return
        if message.content.startswith('$도움말') or message.content.startswith('$help'): 
            await message.channel.send(embed=get_help_embed(helpJson["help"]))
        if message.content.startswith('$공통설정'):
            await message.channel.send(embed=get_common_setting(settingJson))
        if message.content.startswith('$위험방지'):
            await message.channel.send(embed=get_risk_block_setting(settingJson))
        if message.content.startswith('$골든크로스'):
            await message.channel.send(embed=get_golden_cross_setting(settingJson))
        if message.content.startswith('$코인동향'):
            await message.channel.send(embed=get_trend_setting(settingJson))
