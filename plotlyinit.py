import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='harsh.pandey77', api_key='2uwVTl4P0XRo5ZEX93Jh')

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500,2500,1053,500]

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='basic_pie_chart')
