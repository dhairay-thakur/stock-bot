import matplotlib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf


def test_function(company_name):
    df = yf.download(f'{company_name.upper()}.BO', period='1d', progress=False)
    return df

# ticker = yf.Ticker('RELIANCE.BO')

# tsla_df = ticker.history(period="1d")

# print(tsla_df)
# # Reseting the index
# tsla_df = tsla_df.reset_index()
# # Converting the datatype to float
# for i in ['Open', 'High', 'Close', 'Low']:
#     tsla_df[i] = tsla_df[i].astype('float64')

# print(tsla_df['Close'][0])

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
