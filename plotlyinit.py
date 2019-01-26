import plotly.plotly as py
import plotly.graph_objs as go
import json
import plotly

from pprint import pprint

with open("credentials.json") as f:
    credential = json.load(f)

plotly.tools.set_credentials_file(
    username=credential["plotly_username"], api_key=credential["plotly_api_key"]
)

labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
values = [4500, 2500, 1053, 500]

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename="basic_pie_chart")
