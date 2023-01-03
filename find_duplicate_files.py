class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash_map = {}

        for path in paths:
            # split path by " " root/a 1.txt(abcd) => ["root/a","1.txt(abcd)"]

            file_item = path.split() 
            item_path = file_item[0] # "root/a"
            files = file_item[1:] # "1.txt(abcd)"

            for item in files:
                #split "1.txt(abcd)" by ( to get the file

                target_file = item.split("(") # ["1.txt","abcd)"]
                main_file = target_file[-1][:-1] # "abcd"
                sub_path = target_file[0] # "1.txt"
               
                if main_file in hash_map:
                    hash_map[main_file].append(f"{item_path}/{sub_path}")
                else:
                    hash_map[main_file] = [f"{item_path}/{sub_path}"]

        result = []
        for data in hash_map.keys():
            if len(hash_map[data]) >1:
                result.append(hash_map[data])
        return result

