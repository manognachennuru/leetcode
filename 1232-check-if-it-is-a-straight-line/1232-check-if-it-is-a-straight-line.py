class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]
        if x2 == x1:
            #lies in x axis
            axis = x1
            return all(x[0] == x1 for x in coordinates)
        slope = (y2-y1)/(x2-x1)
        
        for i in range(1,len(coordinates)):
            x1,y1 = coordinates[i-1]
            x2,y2 = coordinates[i]
            if x1 == x2:
                return False
            if slope != (y2-y1)/(x2-x1):
                return False
        return True
            
            
            