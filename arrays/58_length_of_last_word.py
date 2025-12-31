'''

Remove extra spaces from the start and the end because the original string may contain the spaces
Split the string 
Count the characters or the length of the last word in the string 

'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s =s.strip()
        word = s.split()
        return(len(word[-1]))
        
