# -*- coding: utf-8 -*-
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        print nums
        for i in xrange(len(nums)):
            real = abs(nums[i])
            real = (real - len(nums)) if real > len(nums) else real
            nums[real-1] = (nums[real-1] - len(nums)) if nums[real-1] < 0 else -nums[real-1]
        return [i+1 for i in xrange(len(nums)) if nums[i] < -len(nums)]
ret = Solution().findDuplicates([10,2,5,10,9,1,1,4,3,7])
print ret