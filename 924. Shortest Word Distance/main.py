class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        p1, p2 = -1, -1
        res = 2**31
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            elif words[i] == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                res = min(res, abs(p1-p2))
            
        return res
