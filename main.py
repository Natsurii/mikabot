import discord
import asyncio
import aiohttp
import os
import time
from discord.ext.commands import Bot
from discord import Game

#vars
BOT_PREFIX = ('>>', 'Nica')
bot = Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
	game = discord.Game("use >>help|Im sux at this")
	await bot.change_presence(status=discord.Status.idle, activity=game)
	print('Hi bwoss! We have already contacted Discord as {0.user}'.format(bot))

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	if message.content.startswith('hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await message.channel.send(msg)

	if message.content.startswith('hi'):
		msg = 'Hi!'.format(message)
		await message.channel.send(msg)

	if message.content.startswith('owo'):
		msg = '*notices* buldge'.format(message)
		await message.channel.send(msg)

	if message.content.startswith('uwu'):
		msg = 'uwu'.format(message)
		await message.channel.send(msg)
		
	if message.content.startswith(BOT_PREFIX):
		await bot.process_commands(message)

@bot.event
async def on_guild_channel_create(channel):
	await channel.send('First! Gotcha!')

@bot.command()
async def calc(ctx, *, argument):
    """Calculate Expressions"""
    message = eval(argument)
    embed = discord.Embed(title='Calculate:'+ str(argument), color=0x65ea15)
    embed.add_field(name='Result', value=(message), inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
	"""Ping latency"""
	start = time.monotonic()
	msg = await ctx.send('Please wait a while...')
	millis = (time.monotonic() - start) * 1000
	# Since sharded bots will have more than one latency, this will average them if needed.
	heartbeat = ctx.bot.latency * 1000
	await msg.edit(content=f':ping_pong: **Pong!** Heartbeat: {heartbeat:,.2f}ms\tACK: {millis:,.2f}ms.')

@bot.command()
async def copyme(ctx, *, content):
    """Repeats a message multiple times."""
    embed = discord.Embed(title='Im a copy-cat bot!', color=0x65ea15)
    embed.add_field(name='You said...', value=content, inline=False)
    await ctx.send(embed=embed)
    	

bot.run(os.environ['TOKEN'])
