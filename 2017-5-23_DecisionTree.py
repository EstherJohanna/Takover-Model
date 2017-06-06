from pyschedule import solvers, plotters, Scenario    
import Sclass

#ToDo: input from GUI
expert = 1
gazeoff = 1 # always means headoff, too!
longgaze = 1 
bodyTurned = 1
Lockout = 0
handsOccupied = 1
distanceHands = 50
feetOnPedals = 0
dangerousScenario = 0
drivingSpeed = 100 #in km/h
perceivedUrgent = 1
S = Scenario('takeover', horizon=20000)

def main():
    #create instance of a situation
    currSituation = Sclass.situation(dangerousScenario, S, distanceHands, drivingSpeed, perceivedUrgent)
    Sclass.situation.resources(currSituation)
    
    #decision tree       
    if not expert:
        if not dangerousScenario:
            Sclass.situation.nov(currSituation)
    else:
        Sclass.situation.exp(currSituation)
        
    Sclass.situation.start(currSituation)
    if not Lockout:
        if not dangerousScenario:
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
    return

if __name__ == '__main__':
    main()
    
#S.use_makespan_objective()
#print(S)
###############################################################################
# A small helper method to solve and plot a scenario
def run(S) :
    #ortools or mip before solve
    if solvers.ortools.solve(S):
        
        plotters.matplotlib.plot(S,fig_size=(150,5))
    else:
        print('no solution exists')
run(S)
