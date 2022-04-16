import csv
import numpy as np
import plotly.express as px

def get_data(data):
    days = []
    marks = []


    with open(data) as file:
        reader = csv.DictReader(file)
        for row in reader:
            days.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))
    
    return{"x": days, "y": marks }

def findcorr(soucre):
    correlation = np.corrcoef(soucre["x"], soucre["y"])
    print(correlation[0,1])


def plotfig(data):
    with open(data) as f:
        df = csv.DictReader(f)
        figure = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
        figure.show()


def setup():
    data_path = "marks and days.csv"
    dataSource = get_data(data_path)
    findcorr(dataSource)
    plotfig(data_path)

setup()