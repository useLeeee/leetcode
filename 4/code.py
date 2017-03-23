class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        offset1 = m // 2
        offset2 = ( m + n ) // 2 - offset1
        ruler = min(m , n) // 2 - 1
        while( (nums1[offset1 - 1] > nums2[offset2] or nums2[offset2 - 1] > nums1[offset1]) and ruler != 0) :
            if( nums1[offset1 - 1] > nums2[offset2] ):
                offset1 = offset1 - ruler
                offset2 = offset2 + ruler
            else:
                offset1 = offset1 + ruler
                offset2 = offset2 - ruler
            ruler = ruler // 2
        if ((m + n) % 2 == 0) :
            return (nums1[offset1]+nums2[offset2])/2
        else :
            return min(nums1[offset1], nums2[offset2])


obj = Solution()
res = obj.findMedianSortedArrays([1,2],[3,4])
                    
