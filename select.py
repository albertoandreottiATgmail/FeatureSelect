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
	
	
#prepare the data set parameters
mySet = SampleSet()
fname = sys.argv[1]
with open(fname) as f:
    defined = False
    while not defined:
        first_line = f.readline()
        for att_val in first_line.split():
            att = Attribute(att_val.split(":")[0])
            att.add("1", "0")
            mySet.addDefinition(att)
        defined = mySet.size() > 1

#prepare the data set itself		
with open(fname) as f:
    line = f.readline()
    while line:
        mySet.addSample(line)
        line = f.readline()
		

#print mySet.parameters		
#select metric
selector = FeatureSelector(sys.argv[2], mySet, '1')
subset = selector.select(int(sys.argv[3]))

#Persist the subset
print subset

with open(sys.argv[4], 'w+') as f:
    for pair in subset:
        f.write(str(pair) + '\n')
