'''


First check the lenghts of the string .If they are equal possiblity of anagrams else return False
Then count how many times each character appeared in s (using dictionary)
Reduce the no of couts of the letter while looping t
At the end all the counts should be zeros for the two strings to be anagram 


'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            count={}
            for i in s:
                count[i] =count.get(i,0)+1

            for i in t:
                count[i] =count.get(i,0)-1


            for val in count.values():
                if val != 0:
                    return False
                
            return True
                
            
            
