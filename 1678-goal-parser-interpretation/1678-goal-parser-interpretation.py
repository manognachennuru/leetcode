class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        output = []
        while i < len(command):
            if command[i] == '(' and command[i+1] == ')':
                output.append('o')
                i += 2
            elif command[i] == '(' and command[i+1] == 'a':
                output.append('al')
                i += 4
            elif command[i] == 'G':
                output.append('G')
                i += 1
                
        return ''.join(output)
                