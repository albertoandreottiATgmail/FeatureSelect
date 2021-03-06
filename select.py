"""
    Feature Selection
"""

from dataManagement import Attribute, SampleSet
from fselector import FeatureSelector
import sys

print sys.argv

#Handle all parameter checking
if len(sys.argv) < 5:
    print 'Too few parametrs, use select filein metric fnum fileout'
    print 'where filein: input file, metric:' + str(FeatureSelector._supported.keys()) + ', fnum: num of features to keep, fileout: output file.'
    sys.exit()
if sys.argv[2] not in FeatureSelector._supported :	
    print 'Unsupported metric type, try one of these: ' + str(FeatureSelector._supported.keys()) 	

try	:
    int(sys.argv[3])
except:
    print 'Error: wrong number of features to keep:' + sys.argv[2] + ', give me a number!'
    sys.exit()

threadNum = 1
try	:
    if len(sys.argv) == 6:
        threadNum = int(sys.argv[5])
except:
    print 'Error: wrong number of features to keep:' + sys.argv[2] + ', give me a number!'
    sys.exit()	
	
#prepare the data set parameters
mySet = SampleSet()
fname = sys.argv[1]

#print mySet.parameters		
#select metric
import time
starttime = time.time()
selectors = []
for id in range(threadNum):
    selectors.append(FeatureSelector(sys.argv[2], id, threadNum))

events = map(lambda x: x.startProcessing(fname), selectors)
map(lambda x:x.wait(), events)

selector = reduce(lambda x, y: x.combine(y), selectors)    
    
subset = selector.select(int(sys.argv[3]))

endtime = time.time()
calcdTime = endtime - starttime
print 'Elapsed time: ' + str(calcdTime)[:-4]

#Persist the subset
print subset

with open(sys.argv[4], 'w+') as f:
    for pair in subset:
        f.write(str(pair[0]) + '\t' + str(pair[1]) + '\n')
