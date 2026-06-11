class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = set()
        for num in numbers: 
            seen.add(num)

        diff = 0
        result = []
        i = 0
        for num in numbers:
            i += 1 
            diff = target - num
            if diff in seen: 
                result.append(i)
                break;

        j = 0
        for num in numbers:
            j += 1
            if num == diff:
                result.append(j)
                break;

        return result

        