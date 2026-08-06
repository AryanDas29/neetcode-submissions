class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26 

            for char in word:
                place = ord(char) - ord('a')
                count[place] += 1 

            key = tuple(count)
            
            if key in groups:
                groups[key] += [word]
            else: 
                groups[key] = [word]
            
        return list(groups.values())


