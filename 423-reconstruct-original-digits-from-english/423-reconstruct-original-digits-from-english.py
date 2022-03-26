class Solution:
    def originalDigits(self, s: str) -> str:
        #zero
        #one - number(o)-2-4-0
        #two - w
        #three - number(t)-2-8
        #four - u
        #five - number(f)- 4
        #six - x
        #seven - number(v) - 5
        #eight - g
        #nine - number(i)-5-6-8
        
        dic = {}
        for ch in s:
            if dic.get(ch):
                dic[ch] += 1
            else:
                dic[ch] = 1
            
        count = [0]*10
        count[0] = dic.get('z',0)
        count[2] = dic.get('w',0)
        count[4] = dic.get('u',0)
        count[6] = dic.get('x',0)
        count[8] = dic.get('g',0)
        count[1] = dic.get('o',0) - count[2] - count[4] - count[0]
        count[3] = dic.get('t',0) - count[2] - count[8]
        count[5] = dic.get('f',0) - count[4]
        count[7] = dic.get('v',0) - count[5]
        count[9] = dic.get('i',0) - count[5] - count[6] - count[8]
        
        output = []
        for i in range(0,len(count)):
            output += [str(i)*count[i]]
            
        return ''.join(output)
    
    
    
    
    
        

        
        
        