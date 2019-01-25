import random
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np

def sumsample100(samplecount=100):
    sample = [i for i in range(1,101)]
    return sum([random.choice(sample) for _ in range(0,samplecount)])/len(sample)


datapoints = [sumsample100(1000) for _ in range(0,1000)]
graph = [go.Histogram(x=datapoints, nbinsx=100)]
py.iplot(graph)

x1 = [sumsample100(1000) for _ in range(0,1000)]
x2 = [sumsample100(1000) for _ in range(0,1000)]
x3 = [sumsample100(1000) for _ in range(0,1000)]

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = ['#333F44', '#37AA9C', '#94F3E4']

# Create distplot with curve_type set to 'normal'
fig = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

# Add title
fig['layout'].update(title='Curve and Rug Plot')

# Plot!
py.iplot(fig, filename='Curve and Rug')
