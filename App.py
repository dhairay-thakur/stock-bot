import matplotlib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf


def update_daily_company(company_name):
    df = yf.download(f'{company_name.upper()}.BO', period='1d', progress=False)
    return df


async def hourly_updates(company_name='WIPRO', duration='1h'):
    ticker = yf.Ticker(f'{company_name}.BO')
    interval = '1d'
    x_name = 'Date'
    if duration[-1] == 'h' or duration == '1d':
        interval = '1m'
        x_name = 'Datetime'
    df = ticker.history(period=duration.lower(), interval=interval)
    # Reseting the index
    df = df.reset_index()
    # Converting the datatype to float
    for i in ['Open', 'High', 'Close', 'Low']:
        df[i] = df[i].astype('float64')
    fig = px.line(df, x=x_name, y='High',
                  title=f'{company_name} Share Prices over last {duration}')
    fig.write_image(f"images/{company_name}.png")


async def hourly_nifty():
    ticker = yf.Ticker('^NSEI')
    df = ticker.history(period="1h", interval='1m')
    # Reseting the index
    df = df.reset_index()
    # Converting the datatype to float
    for i in ['Open', 'High', 'Close', 'Low']:
        df[i] = df[i].astype('float64')
    fig = px.line(df, x='Datetime', y='High',
                  title='Nifty 50 over the last hour')
    fig.write_image("images/nifty.png")


async def daily_nifty():
    ticker = yf.Ticker('^NSEI')
    df = ticker.history(period="6h", interval='1m')
    # Reseting the index
    df = df.reset_index()
    # Converting the datatype to float
    for i in ['Open', 'High', 'Close', 'Low']:
        df[i] = df[i].astype('float64')
    fig = px.line(df, x='Datetime', y='High',
                  title='Nifty 50 performace today')
    fig.write_image("images/nifty.png")
    return (round(df['Open'][0], 2), round(df['Close'][358], 2))
