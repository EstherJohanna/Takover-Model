
#input from GUI
expert = 1
gazeoff = 0 # always means headoff, too!
longgaze = 1
bodyTurned = 0
Lockout = 1
dangerousScenario = 0
perceivedUrgency = 0
handsOccupied = 0
distanceHands = 50
feetOnPedals = 1

from pyschedule import solvers, plotters    
import Sclass
    
    
def main():
    #create instance of a situation
    currSituation = Sclass.situation()
    
    Sclass.situation.start(currSituation)
    
    #decision tree
    if expert:
        Sclass.situation.exp(currSituation)
    else:         Sclass.situation.nov(currSituation)
    Sclass.situation.meaning(currSituation)
    if not Lockout:
        Sclass.situation.lockout(currSituation)
    if gazeoff:  
        Sclass.situation.gazeOnRoad(currSituation)
        if longgaze:
            Sclass.situation.turnSA(currSituation)            
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
    return

if __name__ == '__main__':
    main()
    
Sclass.S.use_makespan_objective()
print(Sclass.S)
#solvers.mip.solve_bigm
###############################################################################
# A small helper method to solve and plot a scenario
def run(S) :
    if solvers.mip.solve(Sclass.S):
        
        plotters.matplotlib.plot(S,fig_size=(40,5))
        #somehow print out the time
    else:
        print('no solution exists')
run(Sclass.S)