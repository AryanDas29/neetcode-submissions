class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen: 
                small, big = min(seen[diff], i), max(seen[diff], i)
                return [small, big]
            seen[num] = i

        