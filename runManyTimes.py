

import DecisionTree
from pyschedule import Scenario
import numpy
import matplotlib.pyplot as plt

results = []

#inputs
a = []
a.append(1) #expert
a.append(0) #gaze off
a.append(1) #long gaze
a.append(0) #body turned
a.append(0) #lockout
a.append(0) #handsOccupied
a.append(0) #distanceHands
a.append(1) #feet on pedals
a.append(1) # dangerous scenario
a.append(130) # driving speed
a.append(1) # perceived urgent
a.append(1) #from 1-3: 1 no task, 2 low mental workload, 3 high mental workload
a.append(1) #traffic: 1 no traffic, 2 medium traffic, 3 much traffic    
    
def main():
    #create instance of a situation
    thisOne = DecisionTree.makeSchedule()
    
    #inputs:(self, inputs, S)
    DecisionTree.makeSchedule.inputs(thisOne, a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10], a[11], a[12], Scenario('takeover', horizon=20000))
    DecisionTree.makeSchedule.main(thisOne)
    results.append(DecisionTree.makeSchedule.run(thisOne))
    



if __name__ == '__main__':
    i = 0
    for i in range (0,1):
        main()
        i += 1
    #print results
    print numpy.mean(results)
    print numpy.std(results)
    plt.hist(results, bins=50)
