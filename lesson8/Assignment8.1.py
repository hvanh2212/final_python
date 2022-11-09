import asyncio
from discord.ext import commands
import requests
"""
Write a Discord bot that

- Send a cat image every 5 minus

- Search cat image with inline command
"""
# get link of random cat image from 'https://some-random-api.ml/img/cat'
def get_cat_pic():
	respone = requests.get('https://some-random-api.ml/img/cat')
	link_json = respone.json()
	link = list(link_json.values())[0]
	return link

bot=commands.Bot(command_prefix='$')
# when client send '$cat', bot send a random cat image
@bot.command(name='cat')
async def send_pic(cxt):
	await cxt.send(get_cat_pic())
# bot auto send a cat imgaes every 5 minis
async def auto_send_pic():
	while True:
		await asyncio.sleep(300)
		# get the channel by ID and send a message to it
		channel = bot.get_channel(987731612001271821)
		await channel.send(get_cat_pic())

bot.loop.create_task(auto_send_pic())
bot.run("OTg3NzMxNzE3Nzg1ODEzMDEy.GWNuKO.Zt9xnShplwTyUQqx7eazAnLp2fVWuBpgaCt45E")
