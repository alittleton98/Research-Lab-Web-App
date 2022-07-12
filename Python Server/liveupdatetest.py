from ipaddress import ip_address
import threading
from turtle import color
from pkg_resources import run_script
import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import threading

X = []
X.append(1)

Y = []
Y.append(1)


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div([
            dcc.Graph
            (
                id='live-graphA', animate=False
            ),
            dcc.Interval
            (
                id='graph-updateA',
                interval=160,
                n_intervals=0
            )
        ]),
        html.Div([
            dcc.Graph
            (
                id='live-graphB', animate=False
            ),
            dcc.Interval
            (
                id='graph-updateB',
                interval=320,
                n_intervals=0
            )
        ])

    ]
)


@app.callback(
    Output('live-graphA', 'figure'),
    [Input('graph-updateA', 'n_intervals')]
)
def update_graph_scatter(n):
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1] * random.uniform(-0.1, 0.1))

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'

    )

    return {'data': [data],
            'layout': go.Layout(xaxis=dict(
                range=[0, 6000]), yaxis=dict(range=[0, max(Y)+.5]),
    )}


@app.callback(
    Output('live-graphB', 'figure'),
    [Input('graph-updateB', 'n_intervals')]
)
def update_graph_scatter(n):
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1] * random.uniform(-0.1, 0.1))

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'

    )

    return {'data': [data],
            'layout': go.Layout(xaxis=dict(
                range=[0, 2000]), yaxis=dict(range=[0, max(Y)+.5]),
    )}


def launchAppA():
    if __name__ == '__main__':
        app.run(debug=True, )


def launchAppB():
    if __name__ == '__main__':
        app.run(port='9854')


threadA = threading.Thread(target=launchAppA)
threadB = threading.Thread(target=launchAppB)


if __name__ == '__main__':
    app.run(debug=True)
