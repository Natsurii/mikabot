import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=",")

@bot.event
async def on_ready():
	print(f'Hi bwoss! We have already contacted Discord as {bot}')

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	if message.content.startswith('hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await message.channel.send(msg)

@bot.event
async def on_guild_channel_create(channel):
	await channel.send('First! Gotcha!')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    output = left + right
    embed = discord.Embed(title='Addition', color=0x65ea15)
    embed.add_field(name='Result', value=str(output), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


bot.run('NDU2NzgzNDAyNDY5OTQ5NDUx.DgVSTA.s9wYTQOElCuwyqgSjBTg99T2Bc4')