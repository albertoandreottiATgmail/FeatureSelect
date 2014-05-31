
"""
    Chi Squared metric
"""
from metric import Metric
from math import log



class ChiSquared(Metric):
    
    def __init__(self, dataset):  # pylint: disable=E1002
        self._dataSet = dataset
        self._classP = {}
        
    def computeMetric(self, att):
        chi2 = 0.0
        #compute mutual information between the class and this attribute
        for value in self._dataSet.parameters[att].getValues():
            subsetT = filter(lambda x: x[att] == value, self._dataSet.values)

            for target in self._dataSet.parameters[0].getValues():
                subsetTC = filter(lambda x: x[0] == target, subsetT)
                NEtEc = float(len(subsetTC))/len(self._dataSet.values)
                
                if target in self._classP.keys():
				    PC = self._classP[target]
                else:
                    PC = float(len(filter(lambda x: x[0] == target, self._dataSet.values)))/len(self._dataSet.values)
                # N x P(t) * P(c)
                EEtEc = len(self._dataSet.values) * float(len(subsetT)/len(self._dataSet.values)) * PC
                chi2 += ((NEtEc - EEtEc) * (NEtEc - EEtEc))/EEtEc

        #do the actual choice according to minfo
        return chi2
        
    
