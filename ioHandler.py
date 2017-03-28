class ioHandler:
    @staticmethod
    def inputHandler():
        '''
        :rtype: array
        '''
        args = raw_input().split(' ')
        args = [eval(x) for x in args]
        return args
    def outputHandler(ret):
        print ret


args = ioHandler.inputHandler()
