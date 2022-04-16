import csv

#Reading data and creating list
with open("height_weight.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

#List for only Weight
new_data = []
for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))

#Mean
n = len(new_data)
sum = 0

for i in new_data:
    sum = sum +i

mean = sum/i
print(mean)

new_data.sort()

#Median
if n % 2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1 + median2) / 2

else:
    median = float(new_data[n//2])

print(median )

#Mode
from collections import Counter

data = Counter(new_data)
moderange = {"50-60":0, "60-70":0, "70-80":0}

for h,c in data.items():
    if 50<float(h)<60:
        moderange["50-60"]+=c
    elif 60<float(h)<70:
        moderange["60-70"]+=c
    elif 70<float(h)<80:
        moderange["70-80"]+=c

mode_range,mode_count = 0,0

for r,c in moderange.items():
    if c > mode_count:
        mode_range, mode_count = [int(r.split("-")[0]), int(r.split("-")[1])], c

mode = float((mode_range[0] + mode_range[1])/2)

print(mode)