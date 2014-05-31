"""
Features Selector
"""

from chisquared import ChiSquared
from mutualinfo import MutualInfo

class FeatureSelector(object):

    _supported = {'chi_squared': ChiSquared,
                  'mutual_inf': MutualInfo}

    def __init__(self, technique, set, tvalue):  # pylint: disable=E1002

        self._tvalue = tvalue
        self._target = 'target'
        
        #fail if wrong argument
        if technique not in self._supported.keys():
            raise ValueError("The technique must be one of" + str(self._supported.keys()))
        
        self._metric = self._supported[technique](set)
        self._dataSet = set
    
	# run selection
    def select(self, k):
        featureSet = []
        
        for att in range(1, len(self._dataSet.parameters)):
            featureSet.append((self._dataSet.parameters[att]._name, self._metric.computeMetric(att)))
        
        featureSet.sort(key = lambda x : x[1])
        featureSet.reverse()
		
		#keep k best 
        return featureSet[0:k]

