import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_result = []
for i in range(1,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)

mean = sum(dice_result) / len(dice_result)
std_deviation = statistics.stdev(dice_result)
#print(std_deviation)
#print(mean)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
#print(median)
#print(mode)
fig = ff.create_distplot([dice_result], ["Results"], show_hist=False)
first_standard_deviation_start, first_standard_deviation_end = mean-std_deviation, mean+std_deviation
second_standard_deviation_start, second_standard_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_standard_deviation_start, third_standard_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_standard_deviation_start, first_standard_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_standard_deviation_end, first_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_standard_deviation_start, second_standard_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_standard_deviation_end, second_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

list_of_first_std = [
                        result for result in dice_result if result > first_standard_deviation_start and result < first_standard_deviation_end
                        ]

list_of_second_std = [
                        result for result in dice_result if result > second_standard_deviation_start and result < second_standard_deviation_end
                        ]

list_of_third_std = [
                        result for result in dice_result if result > third_standard_deviation_start and result < third_standard_deviation_end
                        ]

print("Mean of this data is {}".format(mean))
print("Median of this data {}".format(median))
print("Mode of this data is {}". format(mode))
print("Standard deviation of this data is {}". format(std_deviation))
print("{}% of the data lies within 1 standard deviation".format(len(list_of_first_std) * 100.0/len(dice_result)))
print("{}% of the data lies within 2 standard deviation".format(len(list_of_second_std) * 100.0/len(dice_result)))
print("{}% of the data lies within 3 standard deviation".format(len(list_of_third_std) * 100.0/len(dice_result)))

