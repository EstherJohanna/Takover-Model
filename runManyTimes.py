
import DecisionTree
from pyschedule import Scenario
import numpy
import matplotlib.pyplot as plt

results = []
    
    
def main():
    #create instance of a situation
    thisOne = DecisionTree.makeSchedule()
    
    #inputs:(self, expert, gazeoff, longgaze, bodyTurned, lockout, handsOccupied, distanceHands, feetOnPedals, 
    #dangerousScenario, drivingSpeed, perceivedUrgent, S)
    DecisionTree.makeSchedule.inputs(thisOne, 0, 0, 1, 0, 1, 0, 0, 1, 1, 120, 1, Scenario('takeover', horizon=20000))
    DecisionTree.makeSchedule.main(thisOne)
    results.append(DecisionTree.makeSchedule.run(thisOne))
    



if __name__ == '__main__':
    i = 0
    for i in range (0,1000):
        main()
        i += 1
    #print results
    print numpy.mean(results)
    print numpy.std(results)
    plt.hist(results, bins=50)
