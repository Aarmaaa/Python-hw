import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
stdev = statistics.stdev(data)

print("Population mean --> ", mean)
print("Population stdev --> ", stdev)

def random_set_of_means(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]

        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean
    
mean_list = []

for i in range(0, 100):
    set_of_means = random_set_of_means(30)
    mean_list.append(set_of_means)

sampling_mean = statistics.mean(mean_list)
sampling_stdev = statistics.stdev(mean_list)

first_stdev_start, first_stdev_end = sampling_mean-sampling_stdev, sampling_mean+sampling_stdev
second_stdev_start, second_stdev_end = sampling_mean-(2*sampling_stdev), sampling_mean+(2*sampling_stdev)
third_stdev_start, third_stdev_end = sampling_mean-(3*sampling_stdev), sampling_mean+(3*sampling_stdev)

print("First stdev --> ", first_stdev_start,", ", first_stdev_end)
print("Second stdev --> ", second_stdev_start,", ", second_stdev_end)
print("Third stdev --> ", third_stdev_start,", ", third_stdev_end)

fig = ff.create_distplot([mean_list], ["READING TIME"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))

fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[0, 1], mode="lines", name="SAMPLING MEAN"))

fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 1], mode="lines", name="1ST stdev START"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 1], mode="lines", name="1ST stdev END"))

fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 1], mode="lines", name="2ND stdev START"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 1], mode="lines", name="2ND stdev END"))

fig.add_trace(go.Scatter(x=[third_stdev_start, third_stdev_start], y=[0, 1], mode="lines", name="3RD stdev START"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 1], mode="lines", name="3RD stdev END"))

fig.show()

z_score = (sampling_mean - mean)/sampling_stdev
print(f"Z Score --> {z_score}")