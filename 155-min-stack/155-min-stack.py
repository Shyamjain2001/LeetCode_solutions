class MinStack:

    def __init__(self):
        self.s=[]
        self.ss=[]
    def push(self,val):
        self.s.append(val)
        if self.ss==[]:
            self.ss.append(val)
        else:
            if val<=self.ss[-1]:
                self.ss.append(val)
    def pop(self):
        if self.s==[]: return -1
        if self.s[-1]==self.ss[-1]:
            self.ss.pop()
            return self.s.pop()
        else:
            return self.s.pop()
    def top(self):
        if self.s==[]:
            return -1
        return self.s[-1]
    def getMin(self):
        if self.ss==[]:
            return -1
        else:
            return self.ss[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()