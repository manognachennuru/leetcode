class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # we just need to store least manhattan distance
        # corresponding least index with least manhattan distance
        
        md = 10000
        index = len(points)
        
        for i,point in enumerate(points):
            if x != point[0] and y != point[1]:
                continue
            curr = abs(x-point[0]) + abs(y-point[1])
            if curr < md:
                #found a point with lesser manhattan distance
                md = curr
                index = i
            
            elif curr == md:
                #check if index is lesser
                index = min(i,index)
            
        return index if index != len(points) else -1