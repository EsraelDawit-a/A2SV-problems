class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
       result = []
       kelvin = celsius+273.15
       farenite = (celsius * 1.8) + 32
       result.append(kelvin)
       result.append(farenite)
       return (result)
