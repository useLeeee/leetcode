# -*- coding: utf-8 -*-
"""
ioHandler类主要用于针对不同的OJ进行不同的输入输出处理,输入输出均与leetcode上一致，便于调试错误
注：inputHandler方法中，所有无法识别的输入（无法执行eval函数）均识别为字符串
目前支持的OJ：
1、leetcode
2、华为OJ
"""
__version__ = 1.0


class IoHandler:
    ojtype = "unknown"

    def __init__(self):
        pass

    @staticmethod
    def inputhandler(solution):
        """
        :type devider: string
        :rtype: array
        """
        if IoHandler.ojtype == "leetcode1":
            args1 = raw_input()
            args2 = raw_input()
            args1 = eval(args1)
            args2 = eval(args2)
            ret = []
            if len(args1) != len(args2):
                return "length not the same!"
            else:
                for i in xrange(len(args1)):
                    print i
                    if args1[i] == solution.__class__.__name__:
                        args1[i] = "__init__"
                    ret.append(getattr(solution, args1[i])(*args2[i]))
            print(ret)
            return "finished!"
        elif IoHandler.ojtype == "leetcode2":
            rawargs = raw_input()
            if(rawargs == ""):
                return []
            else:
                args = rawargs.split(" ")
            for x in range(len(args)):
                try:
                    args[x] = eval(args[x])
                except NameError:
                    continue
            ret = solution(*args)
            print ret
