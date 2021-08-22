import asyncio,discord
from discord.ext import commands

token = "NDEyOTEwOTY4NDE5NjQ3NDk5.WoK3Tg.XvYAYiyRQsZDmhg5hrSby70MGS8"
game = discord.Game("개발 중")
bot = commands.Bot(command_prefix='~',status=discord.Status.online,activity=game)

@bot.event
async def on_ready():
    print("봇 가동 성공")

bot.run(token)

