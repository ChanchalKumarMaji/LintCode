class Solution:
    """
    @param point: a list of two-tuples
    @return: a boolean, denote whether the polygon is convex
    """
    def isConvex(self, point):
        # write your code here
        n = len(point)
        last, temp = 0, 0
        for i in range(n):
            p1, p2, p3 = point[(i-1)%n], point[i], point[(i+1)%n]
            v1_x, v1_y = p1[0]-p2[0], p1[1]-p2[1]
            v2_x, v2_y = p3[0]-p2[0], p3[1]-p2[1]
            temp = v1_x*v2_y - v1_y*v2_x
            if temp != 0:
                if last * temp < 0:
                    return False
                last = temp
        
        return True
