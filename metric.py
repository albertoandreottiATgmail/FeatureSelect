

class Metric(object):


    def addDataSet(self, samples):
        raise NotImplementedError("Please Implement this method")

    def computeMetric(self, att):
        raise NotImplementedError("Please Implement this method")

