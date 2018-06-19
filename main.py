import discord
import asyncio
import aiohttp
import os
from discord.ext.commands import Bot
from discord import Game

#vars
BOT_PREFIX = ('>>', '~~')
bot = Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
	game = discord.Game("Serving High Rise")
	await bot.change_presence(status=discord.Status.idle, activity=game)
	print('Hi bwoss! We have already contacted Discord as {0.user}'.format(bot))

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	if message.content.startswith('hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await message.channel.send(msg)

	if message.content.startswith('hi!'):
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
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    output = left + right
    embed = discord.Embed(title='Operation: Addition', color=0x65ea15)
    embed.add_field(name='Result', value=str(output), inline=False)

    await ctx.send(embed=embed)


#@bot.command(pass_context=True)
#async def ping(ctx):
#    t = await bot.say('Pong!')
#    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
#    await bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


bot.run(os.environ['TOKEN'])
