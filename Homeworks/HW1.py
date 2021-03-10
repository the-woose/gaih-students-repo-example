#-------------------------Homework 1-------------------------#
max_range = 10; list_1 = list(range(max_range))
#Question 1
oddList = [i for i in list_1 if i%2==0]
evenList = [i for i in list_1 if i%2==1]
#Question 2
mergedList = [i*2 for i in oddList] + [i*2 for i in evenList]
#Question 3
for i in mergedList: print(i)