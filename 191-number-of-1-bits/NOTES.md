​        #from discussions - 1
        '''If we have number n, then n&(n-1) will remove the rightmost in binary representation of n. For example if n = 10110100, then n & (n-1) = 10110100 & 10110011 = 10110000, where & means bitwize operation and. Very convinient, is it not? What we need to do now, just repeat this operation until we have n = 0 and count number of steps.'''
				
				
				
				#from discussions - 2
        '''to get last digit, you can do (n & 1) 
        and increment count if that last digit is 1'''
