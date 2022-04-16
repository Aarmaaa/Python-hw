import pandas as pd
import plotly.express as px
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

def smaplePicker(counter):
    dataset = []
    for i in range(0, counter):
        random_intex = random.randint(0, len(data)-1)
        value = data[random_intex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean


def setup():
    means = []
    for i in range(0, 100):
        set_of_means = smaplePicker(30)
        means.append(set_of_means)
    showfigure(means)


def showfigure(means):
    df = means
    fig = ff.create_distplot([df], ['reading time'], show_hist = False)
    fig.show()

setup()