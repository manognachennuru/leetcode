class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = [] 
        for a in asteroids:
            result.append(a)
            #compare nth and (n-1)th asteriods
            while len(result) > 1:
                #proceed as long as there's collision
                #if two are facing each other, they'll collide
                if result[-2] > 0 and result[-1] < 0: 
                    #last element is smaller
                    if abs(result[-1]) < abs(result[-2]):
                        result.pop()
                    #last element is bigger
                    elif abs(result[-1]) > abs(result[-2]):
                        result.pop()
                        result.pop()
                        result.append(a)
                    #last two are same
                    else:
                        result.pop()
                        result.pop()
                        
                #break loop if they don't collide
                else:
                    break
        return result
                
            