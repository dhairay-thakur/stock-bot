import os
import time
import discord
import asyncio
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


@bot.command(name='hour', help='HOURLY UPDATES OF THE REQUESTED COMPANY')
async def update_hour(ctx, company_name='^NSEI'):
    await App.hourly_updates(company_name)
    with open(f'images/{company_name}.png', "rb") as fh:
        f = discord.File(fh, filename=f'images/{company_name}.png')
    await ctx.send(file=f)


@tasks.loop(seconds=3)
async def update_hour_nifty():
    await App.hourly_nifty()
    with open('images/nifty.png', "rb") as fh:
        f = discord.File(fh, filename='images/nifty.png')
    channel = bot.get_channel(838120561993056290)
    print(channel)
    await channel.send(file=f)


@update_hour_nifty.before_loop
async def before():
    await bot.wait_until_ready()

update_hour_nifty.start()

bot.run(TOKEN)
