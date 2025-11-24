'''
Source: data.cdc.gov/api/views/bi63-dtpu/rows.csv

View the interactive graph here:
https://rawcdn.githack.com/ekim3483/DataVisualizations/refs/heads/main/plotly/deaths_graph.html

'''

import pandas as pd
import plotly.express as px
import dash
from dash import Dash, dcc, html
from base64 import b64encode
import io


app = dash.Dash(__name__)

buffer = io.StringIO()

data = pd.read_csv('https://data.cdc.gov/api/views/bi63-dtpu/rows.csv', encoding="ISO-8859-1", dtype={'113 Cause Name': str, 'Cause Name': str,	'State': str,})

data = data[data['113 Cause Name'] != 'All Causes']

fig = px.pie(data, values='Deaths', names='113 Cause Name', title='NCHS - Leading Causes of Death in the United States')
fig.write_html(buffer)

html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

app.layout = html.Div([
    html.H4('Simple plot export options'),
    html.P("↓↓↓ try downloading the plot as PNG ↓↓↓", style={"text-align": "right", "font-weight": "bold"}),
    dcc.Graph(id="graph", figure=fig),
    html.A(
        html.Button("Download as HTML"),
        id="download",
        href="data:text/html;base64," + encoded,
        download="deaths_graph.html"
    )
 ])
   
if __name__=='__main__':
    app.run()
