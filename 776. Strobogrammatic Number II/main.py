class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        # write your code here
        res = []
        if n%2 == 0:
            res = [""]
        else:
            res = ["1", "8", "0"]
        
        while n >= 2:
            tmp = res[:]
            res = []
            for s in tmp:
                if n >= 4:
                    res += ["0"+s+"0"]
                res += ["1"+s+"1", "8"+s+"8", "6"+s+"9", "9"+s+"6"]
            n -= 2
        
        return res
