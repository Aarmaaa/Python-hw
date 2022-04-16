import pandas as pd
import plotly.express as px

data = pd.read_csv("covid_data.csv")

grapgh = px.scatter(data, x ="date", y = "cases", color = "country", title = "No. of Covids")
grapgh.show()