# from nextcord.ext import commands

# bot = commands.Bot(command_prefix = "!")

# @bot.command(name = 'hi')
# async def SendMessage(ctx):
#     print("Hello")
#     await ctx.send("hello")

# @bot.event
# async def on_ready():
#     print(f"Logged in as : {bot.user.name}")

# if __name__ == '__main__':
#     bot.run("OTg4MDIzNTcyNzA0NDA3NTky.GB0wuU.LBlvRYD8fAaDyDD1aps4OWVQwjNshQjKYR_uK4")

import asyncio
import discord
from discord.ext import commands
import requests
# respone=requests.get("https://api.thecatapi.com/v1/images/search")
# img_link=respone.json()[0]
bot=commands.Bot(command_prefix='$')
# @bot.command(name='hi')
# async def mess(cxt):
# 	await cxt.send('Hello mate')
# @bot.command(name='catpic')
# async def Cat(cxt):
# 	await cxt.send(img_link['url'])
# @bot.command(name='autocatpic')
# async def AutoCat(cxt):
# 	while True:
# 		await cxt.send('Auto')
# 		await cxt.send(img_link['url'])
# 		await asyncio.sleep(300)
# @bot.event
# async def on_ready(cxt):
#     await cxt.send(f"Logged in as : {bot.user.name}")

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


bot.run("OTg3NzMxNzE3Nzg1ODEzMDEy.GWNuKO.Zt9xnShplwTyUQqx7eazAnLp2fVWuBpgaCt45E")

# print(discord.version_info)