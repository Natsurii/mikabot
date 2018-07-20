#version 3.0
#revised version of this bot framework
#uses code for now on
import discord
import os
import aiohttp
import asyncio
import time
import sys, traceback
from discord.ext import commands
from discord import Game

#vars
version = '3.0 ExpNature'
token = os.environ['TOKEN']

prefixes = ['nica ', 'Nica ','<@456783402469949451> ', 'nica' , 'Nica']
Desc = 'Cool bot uh.'
bot = commands.Bot(command_prefix=prefixes, description=Desc)
initial_extensions = ['cogs.simple',
                      'cogs.members',
                      'cogs.owner']


# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


def is_owner(ctx):
    return ctx.message.author.id == 305998511894167552
    
@bot.command()
@commands.check(is_owner)
async def b(ctx, member):
    msg = await ctx.send('{} ***was banned***'.format(member))
    F = '\N{REGIONAL INDICATOR SYMBOL LETTER F}'
    await msg.add_reaction(F)


@bot.event
async def on_ready():
    game = discord.Game("the n^help command!")
    await bot.change_presence(status=discord.Status.idle, activity=game)    

    print('==========================================================')
    print('.##....##.####..######.....###...........................')
    print('.###...##..##..##....##...##.##........................')
    print('.####..##..##..##........##...##......................')
    print('.##.##.##..##..##.......##.....##...................')
    print('.##..####..##..##.......#########.................')
    print('.##...###..##..##....##.##.....##................')
    print(f'.##....##.####..######..##.....##..............  {version}')
    print('=============================================')
    
    print(f'Veronica Bot ver.{version}')
    print(f'Hi bwoss! We have already contacted Discord! We are inside of {bot.user}\'s account!')

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
    embed.add_field(name='Websocket', value=str("%.2f" %heartbeat) +'ms', inline=True) 
    embed.set_footer(text="Note: Latencies are different to other servers. ") 
    await msg.edit(embed=embed)
bot.run(token, bot=True, reconnect=True)
