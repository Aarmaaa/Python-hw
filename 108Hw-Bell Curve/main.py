import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
weight = df["Avg Rating"].tolist()

fig = ff.create_distplot([weight], ["Avg Rating"], show_hist = False)
fig.show()