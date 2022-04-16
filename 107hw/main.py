import csv
import pandas as pd
import plotly.graph_objects as go

dataframe = pd.read_csv("data.csv")

studentdf = dataframe.loc[dataframe["student_id"] == "TRL_abc"]
groupbylevel = studentdf.groupby("level")["attempt"].mean()

fig = go.Figure(go.Bar(
    x = ["level 1", "level 2", "level 3", "level 4"],
    y = groupbylevel,
))
fig.show()