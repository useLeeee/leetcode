import ""
class Solution:
    def makeNext(self,pattern):
        """
        :type pattern: str
        :rtype:array
        """
        if (len(pattern) == 0):
            return [];
        nextArr = [0 for i in range(len(pattern))]
        nextArr[0] = 0
        compareIndex = 0
        i = 1
        while( i < len(pattern)):
            if(pattern[i] == pattern[compareIndex]):
                compareIndex += 1
                nextArr[i] = compareIndex
                i += 1
            elif(compareIndex != 0):
                compareIndex -= 1
                compareIndex = nextArr[compareIndex]
            else:
                compareIndex = 0
                i += 1
        return nextArr
    def KMP(self,target,pattern):
        '''
        :type pattern: str
        :type target: str
        :rtype: int
        '''
        if(len(pattern)>len(target)):
            return "target length is shorter than pattern length"
        if(not len(target)):
            return "target null"
        nextArr = self.makeNext(pattern)
        j=0
        print nextArr
        for i in range(0,len(target)):
            print i
            if(target[i] == pattern[j]):
                j += 1
            else:
                j=nextArr[j-1]
                i -= 1
            if(j == len(nextArr)):
                return (i,j)
        return "not found"

obj = Solution()
#res = obj.KMP("asd","agctagcagctagctg")
#res = obj.KMP("asd","df")

res = obj.KMP("","")

args = ioHandler.inputHandler()


'''
refer to: http://blog.csdn.net/yearn520/article/details/6729426
'''
