    
import random
import statistics
import plotly.figure_factory as ff

dice_result = []

for i in range(0,1000):
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    dice_result.append(dice_1 + dice_2)

mean = sum(dice_result)/len(dice_result)

std_dev = statistics.stdev(dice_result)
first_devstart, first_devend = mean - std_dev, mean + std_dev

second_devstart, second_devend = mean - (2*std_dev), mean + (2*std_dev)
list_first = [result for result in dice_result
if result > first_devstart and result < first_devend
]

list_second = [result for result in dice_result
if result > second_devstart and result < second_devend
]

third_devstart, third_devend = mean - (3*std_dev), mean + (3*std_dev)
list_third = [result for result in dice_result
if result > third_devstart and result < third_devend
]


print("{}% of data lies within one standard deviation".format(len(list_first)*100.0/len(dice_result)))

print("{}% of data lies within two standard deviation".format(len(list_second)*100.0/len(dice_result)))

print("{}% of data lies within three standard deviation".format(len(list_third)*100.0/len(dice_result)))