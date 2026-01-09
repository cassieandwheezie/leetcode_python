'''
using[2:] removes 0b from the answer 
int(a,2) conerts to binary numbers 


'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a,2)
        decimal_b = int(b,2)
        decimal_sum = decimal_a + decimal_b
        sum1 = bin(decimal_sum)[2:]
        return sum1 
