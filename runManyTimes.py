
import DecisionTree
from pyschedule import Scenario, plotters
import numpy
import matplotlib.pyplot as plt
from scipy.stats import gamma

results = []

#inputs
a = []
a.append(1) #expert
a.append(1) #gaze off
a.append(1) #long gaze
a.append(1) #body turned
a.append(0) #lockout
a.append(1) #handsOccupied
a.append(60) #distanceHands
a.append(0) #feet on pedals
a.append(0) # dangerous scenario
a.append(120) # driving speed
a.append(0) # perceived urgency/ low time budget
a.append(2) #from 1-3: 1 no task, 2 low mental workload, 3 high mental workload
a.append(2) #traffic: 1 no traffic, 2 medium traffic, 3 much traffic    
    
def main():
    #create instance of a situation
    thisOne = DecisionTree.makeSchedule()
    Sc = Scenario('takeover', horizon=20000)

    #inputs:(self, inputs, S)
    DecisionTree.makeSchedule.inputs(thisOne, a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10], a[11], a[12], Sc)
    DecisionTree.makeSchedule.main(thisOne)
    DecisionTree.makeSchedule.run(thisOne)
    results.append(plotters.matplotlib.plot(Sc,img_filename=None,resource_height=1.0,show_task_labels=True, color_prec_groups=False,hide_tasks=[],hide_resources=[],task_colors=dict(),fig_size=(15,5)))



if __name__ == '__main__':
    
    main()
    
    fig, ax = plt.subplots(1, 1)
    r = gamma.rvs(a = 3, loc = results[0] - 3, size=1000)
    ax.hist(r, bins = 50, normed=True, histtype='stepfilled', alpha=0.2)
    ax.legend(loc='best', frameon=False)
    plt.show()

print 'mean is', numpy.mean(r)
#==============================================================================
#     
#     i = 0
#     for i in range (0,100):
#         main()
#         i += 1
#     #print results
#     print numpy.mean(results)
#     print numpy.std(results)
#     plt.hist(results, bins=50)
#==============================================================================
