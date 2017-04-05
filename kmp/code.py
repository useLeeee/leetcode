# coding=utf-8
import sys
sys.path.append("../OJHandler")
from ioHandler import *
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
            #return "target length is shorter than pattern length"
            return "false"
        if(not len(target)):
            #return "target null"
            return "false"
        nextArr = self.makeNext(pattern)
        j=0
        for i in range(0,len(target)):
            if(target[i] == pattern[j]):
                j += 1
            else:
                j=nextArr[j-1]
                i -= 1
            if(j == len(nextArr)):
                #return (i,j-1)
                return "true"
        #return "not found"
        return "false"

obj = Solution()
IoHandler.handler(obj, Solution.__dict__["KMP"], "huawei")
#print 4564367
#res = obj.KMP("asd","agctagcagctagctg")
#res = obj.KMP("asd","df")
#res = obj.KMP()


"""
refer to: http://blog.csdn.net/yearn520/article/details/6729426
"""
"""
尚未测试通过
"""