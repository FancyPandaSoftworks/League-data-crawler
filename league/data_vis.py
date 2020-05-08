import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


champStat = pd.read_csv("champStat.csv")

###VISUALISATION OF THE DATA###

###Function to check data


def statsCheck(stat1, *args):
    arguments = []

    ###level from 0 to 18
    level = np.array(range(19))

    for ar in args:
        arguments.append(ar)

    ###stats of the champs
    champInfo = []
    for i in range(0, champStat.shape[0]):

        ###Bound the information
        if arguments:
            info = (champStat['Champions'][i], champStat[stat1][i], champStat[arguments[0]][i])
        else:
            info = (champStat['Champions'][i], champStat[stat1][i])
        champInfo.append(info)
    #print(champInfo)
    ###Sort the list
    if arguments:
        champInfo.sort(key=lambda tup: (tup[1], tup[2]), reverse=True)
    else:
        champInfo.sort(key=lambda tup: tup[1], reverse=True)

    ###Equation for the first number of champions
    for j in range(0, 20):
        ###Equation
        stat = 0
        levelArg = []
        for k in range(1, len(champInfo[j])):
            if champInfo[j][k] < 6:
                levelArg.append(champInfo[j][k] * level)
                #print(levelArg)
            else:
                stat = stat + champInfo[j][k]
        #print(levelArg)
        #stat = champInfo[j][1] + champInfo[j][2] * level

        #print(stat)
        if len(levelArg) > 1:
            stat = stat + levelArg[0]
            plt.plot(level, stat, label=champInfo[j][0])
        else:
            x = [x[0] for x in champInfo[0:20]]
            y = [x[1] for x in champInfo[0:20]]
            plt.bar(x, y)


#height = [3, 12, 5, 18, 45]
#bars = ('A', 'B', 'C', 'D', 'E')
#y_pos = np.arange(len(bars))

# Create bars
#plt.bar(bars, height)

statsCheck('armor')
plt.legend()
plt.show()
