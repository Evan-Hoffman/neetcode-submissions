class MinStack:
    def __init__(self):
        self.minStack = []
        self.curMin = []
        

    def push(self, val: int) -> None:
        if self.curMin:
            self.curMin.append(min(val, self.curMin[-1]))
        else:
            self.curMin.append(val)

        self.minStack.append(val)
       

    def pop(self) -> None:
        self.curMin.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.minStack[-1]
        
    def getMin(self) -> int:
        return self.curMin[-1]
        




















    # def __init__(self):
    #     self.stack = []
    #     self.minStack = []
        

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if len(self.minStack):
    #         self.minStack.append(min(val, self.minStack[-1]))
    #     else:
    #         self.minStack.append(val)

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.minStack.pop()
        

    # def top(self) -> int:
    #     return self.stack[-1]
        
    # def getMin(self) -> int:
    #     return self.minStack[-1]
        
