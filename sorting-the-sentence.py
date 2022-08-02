class Solution:
    def sortSentence(self, s: str) -> str:
        x = [(int(item[-1]),item[0:-1]) for item in s.split(" ")]
        x.sort()
        s = ""
        for word in x:
            s+= word[-1]+" "
        return f"{s[0:-1]}"