class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 1 and n == 1:
                return False
            else:
                return True
            
        count = 0 
        for i in range(0,len(flowerbed)-1):
            if flowerbed[i] == 1:
                continue
            else:
                if i == 0 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
                elif flowerbed[i-1] == flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
                if count >= n:
                    return True
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            count += 1
            flowerbed[-1] = 1
        if count >= n:
            return True 
        return False
        
                    