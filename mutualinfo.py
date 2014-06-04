
"""
    Mutual Info metric
"""

from metric import Metric
from math import log

class MutualInfo(Metric):
		
    def select(self):

        for att in self._freq.keys():
            for target in [0,1]:
                self._conj[att][target][0] = self._target[target] - self._conj[att][target][1]

        for att in self._freq.keys():
            self._freq[att][0] = self._N - self._freq[att][1]
                
        #print self._conj
        metrics = []
        for att in self._freq.keys():
            metric = 0.0
            for target in [0, 1]:
                for attVal in [0, 1]:
                    probTermClass = self._conj[att][target][attVal]/self._N
                    if probTermClass == 0:
                        continue
                    probTerm = self._freq[att][attVal]
                    #print str(probTermClass) + ' ' + str(probTerm)
                    probClass = self._target[target]
                    metric += probTermClass * log(probTermClass/(probTerm * probClass), 2)
            metrics.append((att, metric))
  
        return metrics

