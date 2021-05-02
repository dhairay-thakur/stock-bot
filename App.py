import matplotlib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf


def test_function(company_name):
    df = yf.download(f'{company_name.upper()}.BO', period='1d', progress=False)
    return df


async def hourly_updates(company_name='WIPRO'):
    ticker = yf.Ticker(f'{company_name}.BO')
    df = ticker.history(period="1h", interval='1m')
    # df = yf.download(f'{company_name.upper()}.BO',
    #                  period='1h', interval='1m', progress=False,)
    # Reseting the index
    df = df.reset_index()
    # Converting the datatype to float
    for i in ['Open', 'High', 'Close', 'Low']:
        df[i] = df[i].astype('float64')
    fig = px.line(df, x='Datetime', y='High',
                  title=f'{company_name} Share Prices in the last hour')
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




# tsla_df = ticker.history(period="1d")

# print(tsla_df)


# tsla_df['Close'].plot(title="TSLA's stock price")

# fig = px.line(tsla_df, x='Date', y='High',
#               title='Apple Share Prices over time (2014)')

# fig.write_image("images/fig1.png")

# fig.show()


# fig = go.Figure([go.Scatter(x=tsla_df['Date'], y=tsla_df['High'])])
# fig.update_xaxes(
#     rangeslider_visible=True,
#     rangeselector=dict(
#         buttons=list([
#             dict(count=1, label="1m", step="month",
#                  stepmode="backward"),
#             dict(count=6, label="6m", step="month",
#                  stepmode="backward"),
#             dict(count=1, label="YTD", step="year",
#                  stepmode="todate"),
#             dict(count=1, label="1y", step="year",
#                  stepmode="backward"),
#             dict(step="all")
#         ])
#     )
# )
# fig.show()
