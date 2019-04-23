'''
Finnian Wengerd
Algorithms
Daniel Showalter
Eastern Mennonite University
Job Scheduling: Stress Level and Optimum Value (TOP-DOWN)
'''
'''
....................................................................................................................................................
Given a sequence of n weeks, the manager must come up with a plan of action with the options:
low-stress, high-stress, or rest resulting in the optimum sequence to bring in the most revenue.

The problem: Given sets of values l1, l2,....ln and h1, h2,....,hn, find a plan of maximum value (revenue).
(Such a plan will be called optimal).
.....................................................................................................................................................
'''
from datetime import datetime
import random

opt_cache = {
            -1:0,                   #This begins the cache with pre-determined values for indexes of i less than 1
            0:0,
            }


'''Recursive function that returns the optimum value of the given parameter i'''
def OPT(i):
    #print(i)
    optimum_i = 0
    #print(i, opt_cache)
    if (opt_cache.get(i)!= None):
        return opt_cache[i], plan
    else:
        optimum_i = max((l[i-1]+OPT(i-1)[0]),(h[i-1]+OPT(i-2)[0]))
        opt_cache[i] = optimum_i
        if optimum_i == (l[i-1]+OPT(i-1)[0]):
            plan[i-1]=("l")
        elif optimum_i == (h[i-1]+OPT(i-2)[0]):
            plan[i-2] = "r"
            plan[i-1]=("h")
        return optimum_i, plan
    


'''Starting function that focuses on integrating each test case and deals with printing out the results (True if the expected result is equal to the optimum value)'''

def My_Print(l,h, expected):
    plan = [0]*len(h)
    starttime = datetime.now()
    return_value = OPT(len(l))
    optimum_value = return_value[0]
    plan = return_value[1]
    #print(optimum_value)
    #print(expected == optimum_value)
    endtime = datetime.now()
    deltaT = endtime-starttime
    totalTime.append(deltaT.total_seconds())
    return deltaT



'''
Start Code
'''

totalTime = []
deltaT = 0
l = []
h=[]
for i in range(50):
    i = random.randint(0,1000)
    l.append(i)

for i in range(50):
    i = random.randint(0,1000)
    h.append(i)
expected = 375477
plan = [0]*len(h)
for i in range(1000):
    My_Print(l,h, expected)

totalseconds = 0
averageTime = 0
for i in totalTime:
    totalseconds +=i
averageTime = (totalseconds/len(totalTime))

print("Average runtime: %f seconds." %(averageTime))
