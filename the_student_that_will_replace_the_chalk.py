class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        l = len(chalk)
        i = 0
        k %= sum(chalk) 
        k %= sum(chalk) 
        while k>0 and chalk[i] <=k:
            k -=chalk[i]
            i+=1
            i%=l
            
        return i