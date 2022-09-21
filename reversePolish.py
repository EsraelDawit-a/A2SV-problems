from math import ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stac = []
        evl = "+-*/"
        
        for i in range(len(tokens)):
            if tokens[i] not in evl:
                stac.append(int(tokens[i]))
            else:
                if len(stac)>=2:
                    
                    num1 = stac[-1]
                    num2 = stac[-2]
                    eq = str(num2)+ tokens[i]+str(num1)
                    
                    stac.pop()
                    stac.pop()
                    if tokens[i] =="/":
                        vl = num2/num1
                        stac.append(ceil(vl) if vl<0 else int(vl))
                    else:
                        stac.append(eval(eq))
        return stac[-1]
      