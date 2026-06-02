class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        detector = set()
        for num in nums:
            if num in detector:
                return True
            else: 
                detector.add(num)
        return False