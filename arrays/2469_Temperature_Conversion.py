'''
This program just converts the given cel temp to kelvin and fahrenheit
'''





class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans=[]
        kelvin = celsius+273.15
        fahrenheit = celsius*1.80+32.00
        return [kelvin,fahrenheit]
        
