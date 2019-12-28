class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.i = 0
        self.j = 0
        self.vec2d = [v for v in vec2d if len(v)>0]
        
    # @return {int} a next element
    def next(self):
        # Write your code here
        res = self.vec2d[self.i][self.j]
        if self.j == len(self.vec2d[self.i]) - 1:
            self.i += 1
            self.j = 0
        else:
            self.j += 1
        return res

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        return self.i < len(self.vec2d)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
