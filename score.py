import pandas as pd
import statistics
import csv


watcher = pd.read_csv('StudentsPerformance.csv')
scoreList = watcher["math score"].to_list()

math_score_mean = statistics.mean(scoreList)
math_score_median = statistics.median(scoreList)
math_score_mode = statistics.mode(scoreList)

print("Mean,Median and Mode of the data is {},{} and {} respectively".format(math_score_mean,math_score_median,math_score_mode))

std_deviation = statistics.stdev(scoreList)

first_std_deviation_start,first_std_deviation_end = math_score_mean-std_deviation,math_score_mean+std_deviation
second_std_deviation_start,second_std_deviation_end = math_score_mean-(2*std_deviation),math_score_mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = math_score_mean-(3*std_deviation),math_score_mean+(3*std_deviation)

thin_1_std_deviation = [result for result in scoreList if result > first_std_deviation_start and result > first_std_deviation_end]
thin_2_std_deviation = [result for result in scoreList if result > second_std_deviation_start and result > second_std_deviation_end]
thin_3_std_deviation = [result for result in scoreList if result > third_std_deviation_start and result > third_std_deviation_end]

print("{}%  of data lies in 1st standard deviation".format(len(thin_1_std_deviation)*100.0/len(scoreList)))
print("{}%  of data lies in 2nd standard deviation".format(len(thin_2_std_deviation)*100.0/len(scoreList)))
print("{}%  of data lies in 3rd standard deviation".format(len(thin_3_std_deviation)*100.0/len(scoreList)))


