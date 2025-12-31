'''
Using a function in python replace("old","new")

'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace(".","[.]")
        return address        
