
#input from GUI
expert = 0
gazeoff = 1 # always means headoff, too!
longgaze = 1 
bodyTurned = 1
Lockout = 0
handsOccupied = 1
distanceHands = 50
feetOnPedals = 0
dangerousScenario = 0
distanceToObstacle = 100 #in m
perceivedUrgency = 0

from pyschedule import solvers, plotters    
import Sclass

def main():
    #create instance of a situation
    currSituation = Sclass.situation()
    #decision tree
    if not dangerousScenario:
        if expert:
            Sclass.situation.exp(currSituation)
        else:         
            Sclass.situation.nov(currSituation)
        Sclass.situation.start(currSituation)
        if not Lockout:
            Sclass.situation.lockout(currSituation)
        if gazeoff:  
            Sclass.situation.gazeOnRoad(currSituation)
            if longgaze:
                Sclass.situation.turnSA(currSituation) 
            if bodyTurned:
                Sclass.situation.turnBody(currSituation)
        if not gazeoff:
            if not longgaze:#if the driver JUST started looking to the street (he does not need
    #to turn the head anymore, but needs to build up situation awareness)
                Sclass.situation.SA(currSituation)
        if handsOccupied:
            Sclass.situation.hands2wheel(currSituation)
            Sclass.situation.unoccupyHands(currSituation)
        if not handsOccupied:
            if distanceHands > 0:
                Sclass.situation.hands2wheel(currSituation)
        if not feetOnPedals:
            Sclass.situation.feet2pedal(currSituation) 
        Sclass.situation.TO(currSituation)
        
    if dangerousScenario:#I expect the tone to be different = driver knows immediately it's dangerous
        Sclass.situation.exp(currSituation)
        Sclass.situation.start(currSituation)
        if gazeoff:  
            Sclass.situation.gazeOnRoad(currSituation)
        if bodyTurned:
                Sclass.situation.turnBody(currSituation)
        if handsOccupied:
            Sclass.situation.hands2wheel(currSituation)
            Sclass.situation.unoccupyHands(currSituation)#change target size!
        if not handsOccupied:
            if distanceHands > 0:
                Sclass.situation.hands2wheel(currSituation)
        if not feetOnPedals:
            Sclass.situation.feet2pedal(currSituation) 
        Sclass.situation.TO(currSituation)
    return

if __name__ == '__main__':
    main()
    
Sclass.S.use_makespan_objective()
print(Sclass.S)
###############################################################################
# A small helper method to solve and plot a scenario
def run(S) :
    #ortools
    if solvers.mip.solve(Sclass.S):
        
        plotters.matplotlib.plot(S,fig_size=(40,5))
    else:
        print('no solution exists')
run(Sclass.S)
