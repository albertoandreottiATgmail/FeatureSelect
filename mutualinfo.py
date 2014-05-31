
"""
    Mutual Info metric
"""

from metric import Metric
from math import log

class MutualInfo(Metric):

    def __init__(self, dataset):  # pylint: disable=E1002
        self._dataSet = dataset
		
    def computeMetric(self, att):
        
        minfo = 0.0
        epsilon = 0.00000001
        
        #compute mutual information between the class and this attribute
        for value in self._dataSet.parameters[att].getValues():
            subset = filter(lambda x: x[att] == value, self._dataSet.values)
            probTerm = float(len(subset))/len(self._dataSet.values)
            
            if probTerm == 0:
                continue
						
            #compute entropy
            entropy = 0.0
            for target in self._dataSet.parameters[0].getValues():
                probClass = float(len(filter(lambda x: x[0] == target, self._dataSet.values)))/len(self._dataSet.values)
                probTermClass = float(len(filter(lambda x: x[0] == target, subset)))/len(subset)
                entropy += probTermClass * log((probTermClass + epsilon)/(probTerm * probClass),  2) 
                    
            #-P(B=b).H(A|B=b)
            minfo += entropy

        #do the actual choice according to minfo
        return minfo

