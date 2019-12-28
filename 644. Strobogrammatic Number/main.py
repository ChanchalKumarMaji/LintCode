class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        d = {
            '0' : '0',
            '1' : '1',
            '6' : '9',
            '8' : '8',
            '9' : '6',
        }
        
        res = ""
        for e in num:
            if e not in d.keys():
                return False
            res += d[e]
        
        return res == num[::-1]
