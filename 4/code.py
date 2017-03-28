class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if( not m):
            if( n%2 ):
                return nums2[n // 2]
            else :
                return (nums2[n // 2] + nums2[n // 2 -1])/2
        if( not n):
            if( n%2 ):
                return nums1[m // 2]
            else :
                return (nums1[m // 2] + nums1[m // 2 -1])/2
        if ( m % 2 == 0 and n % 2 == 0 ):
            offset1 = m // 2
            offset2 = n // 2 -1
        else :
            offset1 = m // 2
            offset2 = n // 2
        ruler = min(m , n) // 2
        while (offset1  and offset2 and offset1<=m and offset2<=n and ruler) :
            if( nums1[offset1 - 1] > nums2[offset2] ):
                offset1 = offset1 - ruler
                offset2 = offset2 + ruler
                if (nums1[offset1+1] > nums2[offset2] and nums2[offset2 - 1] < nums1[offset1]):
                    break
            else:
                offset1 = offset1 + ruler
                offset2 = offset2 - ruler
                if (nums2[offset2+1] > nums1[offset1] and nums1[offset1 - 1] < nums2[offset2]):
                    break
            ruler = ruler // 2
        if ((m + n) % 2 == 0) :
            return (nums1[offset1]+nums2[offset2]) / 2
        else :
            return min(nums1[offset1], nums2[offset2])


obj = Solution()
res = obj.findMedianSortedArrays([],[1])
print res
