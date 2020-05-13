import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# name    exectimes   ticketnum   time
# lottery
df = pd.read_csv("lottery.csv", sep='\t',lineterminator='\n')
min = 99999
max = 0
for index,row in df.iterrows():
    if min > row['time']:
        min = row['time']
    if max < row['time']:
        max = row['time']
df['time'] -= min
df['exectimes'] -= 8
max = max-min

fig = px.scatter(df, x = 'time', y = 'exectimes', title='Lottery Scheduling')

x = np.arange(max)
fig.add_trace(go.Scatter(x=x, y=x*0.503, name='prog1'))
fig.add_trace(go.Scatter(x=x, y=x*0.333, name='prog2'))
fig.add_trace(go.Scatter(x=x, y=x*0.169, name='prog3'))

fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    xaxis_title="Time spent",
    yaxis_title="Number of executed times",
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor="LightSteelBlue",
)
fig.show()



# stride
df = pd.read_csv("stride.csv", sep='\t',lineterminator='\n')
min = 99999
max = 0
for index,row in df.iterrows():
    if min > row['time']:
        min = row['time']
    if max < row['time']:
        max = row['time']
df['time'] -= min
df['exectimes'] -= 8
max = max-min
fig = px.scatter(df, x = 'time', y = 'exectimes', title='Stride Scheduling')

x = np.arange(max)
fig.add_trace(go.Scatter(x=x, y=x*0.503, name='prog1'))
fig.add_trace(go.Scatter(x=x, y=x*0.333, name='prog2'))
fig.add_trace(go.Scatter(x=x, y=x*0.169, name='prog3'))

fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    xaxis_title="Time spent",
    yaxis_title="Number of executed times",
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor="LightSteelBlue",
)
fig.show()