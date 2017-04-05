class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        lennow = 0
        if len(nums) == 0:
            return 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                maxlen = lennow if maxlen < lennow else maxlen
                lennow = 0
            else:
                lennow += 1
        maxlen = lennow if maxlen < lennow else maxlen
        return maxlen
obj = Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])
