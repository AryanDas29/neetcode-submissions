class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        for x in s:
            if x in countS:
                countS[x] += 1
            else:
                countS[x] = 1

        for y in t:
            if y in countT:
                countT[y] += 1
            else:
                countT[y] = 1

        return countT == countS