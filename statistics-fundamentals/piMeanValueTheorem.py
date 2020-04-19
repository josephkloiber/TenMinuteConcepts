#!/Users/josephkloiber/anaconda3/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import random

diceCount = 5000
rollCount = 500
diceRolls = []
meansPerDice = []

################################################################################
# Roll N 6 sided die M times.
for dice in range(diceCount):
    outcomes = []
    for roll in range(rollCount):
        outcomes.append(random.randint(1,6))
    diceRolls.append(outcomes)
    # compute the means for each die
    meansPerDice.append(np.average(outcomes))

plt.figure(1) # Sample Histogram
# pick a dice from the list
sample = random.randint(0,diceCount-1)
plt.title("Sample Distribtion "+str(sample)+" | "+str(rollCount)+" Rolls")
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.hist(diceRolls[sample], 6, facecolor='purple')

plt.figure(2) # Means
plt.title("Arithmetic mean for each Dice at " + str(rollCount) + " Rolls")
expectedValue = np.zeros([2, 2])
expectedValue[0] = ([0, 3.5])
expectedValue[1] = ([diceCount, 3.5])
plt.xlim(0, diceCount)
plt.ylim(0, 6)
plt.xlabel("Dice Number")
plt.ylabel("Mean")
plt.plot(meansPerDice, 'ko')
plt.plot(expectedValue[:,0], expectedValue[:,1], 'r-')

plt.figure(3) # Histogram of the Means
plt.title("Distribution of Arithmetic Means")
plt.hist(meansPerDice, 50, facecolor='purple')

# plot the estimated normal curve
plt.figure(4)

x = []
start = 3000
for i in range(start,start + 2000):
    x.append(start + s

# mom = np.average(meansPerDice) # Mean Of Means
# som = np.sqrt(np.var(meansPerDice)) # Std. Dev of Means
# truthNormal=[]
# #generate the independent variables
# start = 3
# indVariable = []
# indVariable.append(3)
# for i in range(2000):
    # indVariable.append(
# for i in range(3,5):
    # term1 = 1 / (som * np.sqrt(2 * np.pi))
    # truthNormal.append(term1 * np.exp(-0.5*((i - mom)/som)**2))
# plt.plot(truthNormal)
################################################################################

plt.show()
