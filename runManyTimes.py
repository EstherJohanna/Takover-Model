
import DecisionTree
from pyschedule import Scenario


    
    
def main():
    #create instance of a situation
    thisOne = DecisionTree.makeSchedule()
    
    DecisionTree.makeSchedule.inputs(thisOne, 0,1,1,1,1,1,50,1,1,100,0,Scenario('takeover', horizon=20000))#(self, expert, gazeoff, longgaze, bodyTurned, lockout, handsOccupied, distanceHands, feetOnPedals, dangerousScenario, drivingSpeed, perceivedUrgent, S)
    DecisionTree.makeSchedule.main(thisOne)
    DecisionTree.makeSchedule.run(thisOne)



if __name__ == '__main__':
    i = 0
    for i in range (0,3):
        main()
        i += 1