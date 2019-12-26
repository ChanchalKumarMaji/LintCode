from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.q = deque([])
        self.s = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        k = 0
        if len(self.q) == self.size:
            k = self.q.popleft()
        self.q.append(val)
        self.s += val - k
        return self.s / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
