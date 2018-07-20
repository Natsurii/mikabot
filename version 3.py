#version 3.0
#revised version of this bot framework
#uses code for now on
import discord
import os
import aiohttp
import asyncio
import sys, traceback
from discord.ext import commands
from discord import Game

#vars
version = '3.0 ExpNature'
#token = os.environ['TOKEN']
token = 'NDU2Nzg0OTY1NzMzMTg3NTg0.DhEsGg.BPy6Q3hJekl2x4hKL2OWYOUBh8k' #remove this part before uploading

def get_prefix(bot, message):

    prefixes = ['n^', 'N^']
# Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
# Only allow ? to be used in DMs
        return '?'
# If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix=get_prefix)
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


'''@bot.command()
@commands.check(owner)
async def disconnect(ctx):
    await ctx.send(f'Goodbye Senpai {ctx.author} umu')
    print(f'Bot was disconnected by {ctx.author}')
    #await ctx.bot.logout()'''


bot.run(token, bot=True, reconnect=True)