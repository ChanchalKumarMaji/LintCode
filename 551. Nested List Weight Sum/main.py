"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

from collections import deque

class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        res = 0
        q = deque(nestedList)
        f = 1
        while len(q) != 0:
            k = len(q)
            while k != 0:
                u = q.popleft()
                if u.isInteger():
                    res += f * u.getInteger()
                else:
                    temp = u.getList()
                    for v in temp:
                        q.append(v)
                k -= 1
            f += 1
        
        return res
