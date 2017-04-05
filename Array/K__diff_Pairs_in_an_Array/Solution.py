class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        diff = {}
        ret = 0
        if k < 0:
            return ret
        for x in range(len(nums)):
            if nums[x] in diff:
                diff[nums[x]] += 1
            else:
                diff[nums[x]] = 1
        for x in diff:
            if k == 0:
                ret += 1 if diff[x] > 1 else 0
            elif x+k in diff:
                ret += 1
        return ret
obj = Solution()
ret, diff = obj.findPairs([1, 3, 1, 4, 5], 0)

