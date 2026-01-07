class Solution:
    def addDigits(self, num: int) -> int:
        sum=0
        while(num!=0):
            last_digit = num%10
            sum = sum+last_digit
            num = num//10
        while(sum>=10):
            temp =0
            while sum!=0:
                last_digit = sum%10
                temp = temp+last_digit
                sum = sum//10
            sum =temp
        return sum
        

    
