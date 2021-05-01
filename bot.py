import os
import time
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks

import App

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(
        f'{bot.user.name} is connected successfully!'
    )


@bot.event
async def on_member_join(member):
    await message.channel.send(f'Hi {member.name}, welcome to my Discord server!')


@bot.command(name='eod', help='END OF DAY DATA FOR REQUESTED COMPANY')
async def update(ctx, company_name='RELIANCE.BO'):
    data = App.test_function(company_name)
    response = f'{company_name.upper()} EOD Data -\n - '
    response += '\n - '.join(
        [f'{field}: {round(data[field][0],2)}' for field in data])
    await ctx.send(response)


bot.run(TOKEN)
