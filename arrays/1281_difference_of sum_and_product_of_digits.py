'''
Rememeber-
The frst way 
We cannot loop on integers like if I have 2345 i cannot apply for loop on it and exact the digits directly 
like - for i in n :
this is wrong 
the correct way is to eithr convert this in string or do in mathematical way to extract the digits of the number 


The second way
in python / does the float division but the condition in while is for int so it expects n to stay as integer 
So, use //

'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
       
        product =1
        sum =0
        for i in n:
            i = int(i)
            product = product*i
            sum =sum+i
        return (product-sum)





'''
This is the another way 
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product =1
        sum =0
        while(n>0):
            digit = n%10
            sum = sum+digit
            product = product*digit
            n=n//10

        return product-sum 
