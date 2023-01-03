class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # track their lossing record
        hash_map = {}
        for i in range(len(matches)):
            winner,loser = matches[i]
            hash_map[loser] = hash_map.get(loser,0)+1
            if winner not in hash_map:
                hash_map[winner] = 0
         
        new_map = sorted(hash_map.items())
        no_lose = []
        one_lose = []
        for item in new_map:
            if item[-1] == 0:
                no_lose.append(item[0])
            if item[-1] == 1:
                one_lose.append(item[0])
        return [no_lose,one_lose]

            
