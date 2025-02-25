'''
    155. Min Stack
'''

# 84.18% | 6.87%
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) > 0:
            val_min = min(self.stack[-1][1], val)
            self.stack.append([val, val_min])
        else:
            self.stack.append([val, val])
        

    def pop(self) -> None:
        ret = self.stack[-1]
        self.stack = self.stack[:-1]
        return ret

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()