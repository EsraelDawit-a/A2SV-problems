class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        self.l = []
        for i in range(n):
            if (i+1)%3 == 0 and (i+1)%5 ==0:
                self.l.append("FizzBuzz")
            elif (i+1)%3 ==0:
                self.l.append("Fizz")
            elif (i+1)%5 == 0:
                self.l.append("Buzz")
            else:
                self.l.append(f"{i+1}")
                
        return self.l