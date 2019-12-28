class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        res = []
        for i in range(1, len(s)):
            if s[i] == s[i-1] == '+':
                res.append(s[:i-1] + '--' + s[i+1:])
        
        return res
