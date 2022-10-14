class Solution:
    def compress(self, chars: List[str]) -> int:
        c = 1
        for i in range(len(chars)-1,-1,-1):
            if i and chars[i] == chars[i-1]:
                c+=1
                chars.pop(i)
            else:
                if c >1:
                    for it in str(c)[::-1]:
                        chars.insert(i+1, it)
                    c = 1
     

        # chars[:] = s
        # return len(chars)