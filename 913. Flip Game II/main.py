class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    def CanWin(self, s, d):
        if s in d.keys():
            return d[s]
        for i in range(1, len(s)):
            if s[i-1] == s[i] == '+':
                opponent = s[:i-1] + '--' + s[i+1:]
                if(not self.CanWin(opponent, d)):
                    d[s] = True
                    return True
        d[s] = False
        return False
        
    def canWin(self, s):
        # write your code here
        if len(s) < 2:
            return False
        d = {}
        return self.CanWin(s, d)
