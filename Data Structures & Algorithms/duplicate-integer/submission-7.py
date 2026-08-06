class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
                #there is a duplicate
            else: 
                seen.add(num)

        return False
       