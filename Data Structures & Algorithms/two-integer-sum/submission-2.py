class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        for i, val in enumerate(nums):
            diff = target - val
            if diff in seen:
                j = seen[diff]
                return [min(i, j), max(i, j)]
            seen[val] = i
        return []
            
        
      

        
        