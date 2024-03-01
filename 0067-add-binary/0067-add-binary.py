class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #similar to plus one, but here we have a string
        #we can't reverse like we did there
        #no need to convert back to integers 

        #make them have same length
        if len(a) < len(b):
            zeroes = "0" * (len(b) - len(a))
            a = zeroes + a

        if len(a) > len(b):
            zeroes = "0" * (len(a) - len(b))
            b = zeroes + b

        result = deque([])

        carry = "0"
        p1 = len(a) - 1
        p2 = len(b) - 1
        while p1 >= 0 and p2 >= 0:
            #need to add three values
            toadd = [a[p1], b[p2], carry]
            #three "1"s
            if toadd.count("1") == 3:
                result.appendleft("1")
                carry = "1"
            #two "1"s
            if toadd.count("1") == 2:
                result.appendleft("0")
                carry = "1"
            #one "1"
            if toadd.count("1") == 1:
                result.appendleft("1")
                carry = "0"
            #zero "1"
            if toadd.count("1") == 0:
                result.appendleft("0")
                carry = "0"
            p1 -= 1
            p2 -= 1

        if p1 == -1 and p2 == -1:
            # a and b are done, there could be carry
            if carry == "1":
                result.appendleft("1")
            return ''.join(list(result))

            