class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        i = 0
        num = 0
        for c in abbr:
            if c.isdigit():
                if num == 0 and c == '0':
                    return False
                num = num * 10 + int(c)
            else:
                i += num
                if c != word[i]:
                    return False
                i += 1
                num = 0
        if num != 0 and i + num != len(word):
            return False
        
        return True
