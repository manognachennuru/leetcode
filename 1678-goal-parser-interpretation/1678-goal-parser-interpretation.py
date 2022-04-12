class Solution:
    def interpret(self, command: str) -> str:
        dic = {"G":"G", "()":"o","(al)":"al"}
        
        output = []
        tmp = ""
        for i in range(0,len(command)):
            tmp += command[i]
            if tmp in dic:
                output.append(dic[tmp])
                tmp = ""
            
                
        return ''.join(output)
                