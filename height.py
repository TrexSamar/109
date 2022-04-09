
import pandas as pd
import statistics
import csv

df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

print('mean, mode and median of height is:{},{}and{} resectively'.format(height_mean, height_mode, height_median))
print('mean, mode and median of w\eight is:{},{}and{} resectively'.format(weight_mean, weight_mode, weight_median))

std_dev = statistics.stdev(height_list)
first_devstart, first_devend = height_mean - std_dev, height_mean + std_dev

list_first = [result for result in height_list
if result > first_devstart and result < first_devend
]

second_devstart, second_devend = height_mean - (2*std_dev), height_mean + (2*std_dev)
list_first = [result for result in height_list
if result > first_devstart and result < first_devend
]

list_second = [result for result in height_list
if result > second_devstart and result < second_devend
]

third_devstart, third_devend = height_mean - (3*std_dev), height_mean + (3*std_dev)
list_third = [result for result in height_list
if result > third_devstart and result < third_devend
]
print("{}% of data lies within one standard deviation".format(len(list_first)*100.0/len(height_list)))

print("{}% of data lies within two standard deviation".format(len(list_second)*100.0/len(height_list)))

print("{}% of data lies within three standard deviation".format(len(list_third)*100.0/len(height_list)))