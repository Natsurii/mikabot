import discord
import asyncio
import aiohttp
import os
import time
from discord.ext import commands
from discord import Game

#vars
BOT_PREFIX = ['Nica ','nica ']
bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
	game = discord.Game("use Nica help | @vduterteee")
	await bot.change_presence(status=discord.Status.idle, activity=game)
	print('Hi bwoss! We have already contacted Discord as {0.user}'.format(bot))

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	if message.content.startswith('hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await message.channel.send(msg)

	if message.content.startswith('owo'):
		msg = '*notices* bulge'.format(message)
		await message.channel.send(msg)

	if message.content.startswith('uwu'):
		msg = 'uwu'.format(message)
		await message.channel.send(msg)
		
	await bot.process_commands(message)
		
@bot.command()
async def ping(ctx):
	"""Ping latency"""
	start = time.monotonic()
	msg = await ctx.send(':ping_pong:Pong!')
	millis = (time.monotonic() - start) * 1000
	# Since sharded bots will have more than one latency, this will average them if needed.
	heartbeat = ctx.bot.latency * 1000
	embed=discord.Embed(title="Bot Latency", description="The bot received your latency request.", color=0xe7aeff) 
	embed.set_thumbnail(url="https://emojipedia-us.s3.amazonaws.com/thumbs/320/apple/129/table-tennis-paddle-and-ball_1f3d3.png")
	embed.add_field(name='ACK', value=str("%.2f" %millis) + ' ms', inline=False) 
	embed.add_field(name='Heartbeat', value=str("%.2f" %heartbeat) +'ms', inline=True) 
	embed.set_footer(text="Note: Latencies are different to other servers. ") 
	await msg.edit(embed=embed)
	
@bot.command()
async def copyme(ctx, *, content):
    """Repeats a message multiple times."""
    embed = discord.Embed(title='Im a copy-cat bot!', color=0x65ea15)
    embed.add_field(name='You said...', value=content, inline=False)
    await ctx.send(embed=embed)
	
def owner(ctx):
    return ctx.message.author.id == 305998511894167552
    
@bot.command()
@commands.owner()
async def b(ctx, member):
    msg = await ctx.send('{} ***was banned***'.format(member))
    F = '\N{REGIONAL INDICATOR SYMBOL LETTER F}'
    await msg.add_reaction(F)

@bot.command(name='eval')
@commands.owner()
async def _eval(ctx, *, code):
    """A bad example of an eval command"""
    await ctx.send(eval(code))
	
bot.run(os.environ['TOKEN'])
