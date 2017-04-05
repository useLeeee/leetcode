# -*- coding: utf-8 -*-
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(0, len(nums)):
            if nums[i] == i+1:
                pass
            else:
                nextindex = nums[i] - 1
                nums[i] = -1
                i = nextindex
                while nums[i] != i+1 and nums[i] != -1:
                    nextindex = nums[i]-1
                    nums[i] = i+1
                    i = nextindex
                nums[i] = i+1
        for i in range(0, len(nums)):
            if nums[i] != i+1:
                ret.append(i+1)
        return ret,nums
obj = Solution()
ret, nums = obj.findDisappearedNumbers([1,1])
