class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxlen = 0
        dic = {}
        if not len(s):
            return 0
        for end in range(0,len(s)):
            if ( dic.has_key(s[end]) and dic[s[end]] >= start ):
                if( (end - start) > maxlen):
                    maxlen = end - start
                start = dic[s[end]] + 1
                dic[s[end]] = end
                end = end + 1
            else:
                dic[s[end]] = end
                end = end + 1
        if ((end - start) > maxlen):
             maxlen = end - start
        return maxlen
obj = Solution()
res = obj.lengthOfLongestSubstring("pwwkew")
