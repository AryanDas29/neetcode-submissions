class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [min(i, seen[diff]), max(seen[diff], i)]
            seen[n] = i
        return []

         
            
            