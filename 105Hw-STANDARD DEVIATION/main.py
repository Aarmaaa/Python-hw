import math
import csv

with open("data.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#file_data.pop(0)

#List containing all the marks
data = file_data[0]

#Step 1 : Finding Mean
def mean(data):
    n = len(data)
    sum = 0

    for i in data:
        sum = sum + int(i) 

    mean = sum/n
    return mean

#Step 2: Subtracting mean from all the values & squaring them

squarelist = []

for i in data:
    a = int(i) - mean(data) 
    a = a**2
    squarelist.append(a)

#Step 3: Sum of squred list 

sum = 0
for i in squarelist:
    sum = sum + i

#step 4: Divied by total values

result = sum/len(data)

#step 5: square root of result

stdev = math.sqrt(result)

print(stdev)
