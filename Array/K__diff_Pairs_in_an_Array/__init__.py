__author__ = 'qianjie'
__bestanswer__ = """def findPairs(self, nums, k):
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0"""
__no__ = 532
