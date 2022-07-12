from ipaddress import ip_address
import threading
from turtle import color, title
import pandas
from pkg_resources import run_script
import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly
import random

from collections import deque
import threading

dashApp = dash.Dash(__name__)

# bar graph
barGraphDataFrame = pandas.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

barGraph = plotly.graph_objs.Bar(
    barGraphDataFrame, x="Fruit", y="Amount", color="City", barmode="Group")

scatterDataFrame = plotly.data.iris()
scatterPlot = plotly.graph_objs.Scatter(
    scatterDataFrame, x="sepal_width", y="sepal_length", title="Scatter Plot")

lineDataFrame = scatterDataFrame
lineGraph = plotly.graph_objs.Line(
    lineDataFrame, x="petal_width", y="petal_length", title="Line Graph")
