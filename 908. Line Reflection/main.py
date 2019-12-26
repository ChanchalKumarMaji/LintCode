class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """
    def isReflected(self, points):
        # Write your code here
        if not points:
            return True
        s = set()
        minX = maxX = points[0][0]
        for p in points:
            minX = min(minX, p[0])
            maxX = max(maxX, p[0])
            s.add(str(p[0]) + '#' + str(p[1]))
        for p in points:
            if str(minX + maxX - p[0]) + '#' + str(p[1]) not in s:
                return False
        
        return True
