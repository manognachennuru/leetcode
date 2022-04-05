class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        #manhattan = [least manhattan distance, corresponding least index with least manhattan distance]
        manhattan = [10000, len(points)]
        
        for i,point in enumerate(points):
            if x != point[0] and y != point[1]:
                continue
            curr = abs(x-point[0]) + abs(y-point[1])
            if curr < manhattan[0]:
                #found a point with lesser manhattan distance
                manhattan[0] = curr
                manhattan[1] = i
            
            elif curr == manhattan[0]:
                #check if index is lesser
                manhattan[1] = min(i,manhattan[1])
            
        return manhattan[1] if manhattan[1] != len(points) else -1