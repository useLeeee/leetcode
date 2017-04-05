class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        time = 0
        if not len(timeSeries):
            return 0
        if len(timeSeries) ==1 :
            return duration
        for i in range(1, (len(timeSeries))):
            if(timeSeries[i-1]+duration < timeSeries[i]):
                time += duration
            else:
                time += timeSeries[i] - timeSeries[i-1]
        time += duration
        return time
