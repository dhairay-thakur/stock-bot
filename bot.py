import os
import time
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
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
    scheduler = AsyncIOScheduler()

    # Scheduled for hourly nifty updates from 10:30 - 14:30
    scheduler.add_job(update_hour_nifty, CronTrigger(
        day_of_week="0-4", hour="10-15", minute="30"))

    # Scheduled for daily nifty update at 15:35
    scheduler.add_job(update_daily_nifty, CronTrigger(
        day_of_week="0-4", hour="15", minute="35"))

    scheduler.start()


@bot.event
async def on_member_join(member):
    await message.channel.send(f'Hi {member.name}, welcome to my Discord server!')


@bot.command(name='eod', help='END OF DAY DATA FOR REQUESTED COMPANY (Name)- https://in.finance.yahoo.com/')
async def update(ctx, company_name='RELIANCE.BO'):
    data = App.update_daily_company(company_name)
    response = f'{company_name.upper()} EOD Data -\n - '
    response += '\n - '.join(
        [f'{field}: {round(data[field][0],2)}' for field in data])
    await ctx.send(response)


@bot.command(name='price', help='PRICE VARIATION OF THE REQUESTED COMPANY (Name,Duration)- https://in.finance.yahoo.com/')
async def update_hour(ctx, company_name='RELIANCE', duration='1y'):
    await App.hourly_updates(company_name, duration)
    with open(f'images/{company_name}.png', "rb") as fh:
        f = discord.File(fh, filename=f'images/{company_name}.png')
    await ctx.send(file=f)


async def update_hour_nifty():
    await App.hourly_nifty()
    with open('images/nifty.png', "rb") as fh:
        f = discord.File(fh, filename='images/nifty.png')
    channel = bot.get_channel(838120561993056290)
    await channel.send(file=f)


async def update_daily_nifty():
    result = await App.daily_nifty()
    with open('images/nifty.png', "rb") as fh:
        f = discord.File(fh, filename='images/nifty.png')
    channel = bot.get_channel(838120561993056290)
    await channel.send(file=f)
    await channel.send(f'Nifty 50 \n -Open = {result[0]} \n -Close={result[1]} \n -Change={round(result[1] - result[0],2)}')


bot.run(TOKEN)
