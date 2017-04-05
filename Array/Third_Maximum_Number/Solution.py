class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > maxnum[0]:
                maxnum.insert(0, nums[i])
            elif nums[i] == maxnum[0]:
                continue
            elif len(maxnum) < 2 or nums[i] > maxnum[1]:
                maxnum.insert(1, nums[i])
            elif nums[i] == maxnum[1]:
                continue
            elif len(maxnum) < 3 or nums[i] > maxnum[2]:
                maxnum.insert(2, nums[i])
        if len(maxnum) > 2:
            return maxnum[2]
        else:
            return maxnum[0]

