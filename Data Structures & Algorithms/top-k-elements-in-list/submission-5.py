class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1

        curr = k 
        while curr > 0:
            current_max = max(count.values())
            for num in count:
                if count[num] == current_max:
                    res.append(num)
                    count[num] = -1
                    curr -= 1

        return res
        