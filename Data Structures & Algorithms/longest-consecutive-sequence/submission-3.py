class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set()
        for num in nums:
            seq.add(num)

        
        longest = 0
        for num in nums:
            if (num - 1) not in seq:
                curr = num
                length = 1
                while (curr + 1) in seq:
                    curr += 1
                    length += 1
                    
                longest = max(longest, length)

     

        return longest
            
        