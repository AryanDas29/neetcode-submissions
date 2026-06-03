class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        output = []

        prefixCount = 1
  
        for num in nums:
            prefix.append(prefixCount)
            prefixCount = prefixCount * num
            
        suffixCount = 1
        for num in reversed(nums):
            suffix.append(suffixCount)
            suffixCount *= num

        suffix.reverse()

        i = 0
        for num in nums:
            output.append(prefix[i] * suffix[i])
            i += 1

        return output




