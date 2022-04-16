from operator import mod
import random
import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
readscore = df["reading score"].to_list()

mean = st.mean(readscore)
median = st.median(readscore)
mode = st.mode(readscore)
stdev = st.stdev(readscore)

first_start, first_end = mean - stdev, mean + stdev
second_start, second_end = mean - (2*stdev), mean + (2*stdev)
third_start, third_end = mean - (3*stdev), mean + (3*stdev)

readscore_within_first_stdev = [result for result in readscore if result > first_start and result < first_end]
readscore_within_second_stdev = [result for result in readscore if result > second_start and result < second_end]
readscore_within_third_stdev = [result for result in readscore if result > third_start and result < third_end]

print("{}% of data lies within first stdev ".format(len(readscore_within_first_stdev)*100/len(readscore)))
print("{}% of data lies within second stdev ".format(len(readscore_within_second_stdev)*100/len(readscore)))
print("{}% of data lies within third stdev ".format(len(readscore_within_third_stdev)*100/len(readscore)))