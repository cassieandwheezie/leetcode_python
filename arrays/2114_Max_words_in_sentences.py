'''
Sentences is a dictionary and we have to find the maximum number of words in a sentence
split the sentences by loop and then split the words in a sentence and find the max words

'''
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for i in sentences:
            word = len(i.split())
            max_words = max(max_words,word)
        return max_words

            
        
