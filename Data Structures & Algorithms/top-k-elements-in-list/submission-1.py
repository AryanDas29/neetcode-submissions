class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = {}
        answer = []
        for i in nums:
            if i in hashset:
                hashset[i] += 1
            else:
                hashset[i] = 1 
        
    

        while k > 0:
            value_to_remove = max(hashset.values())
            keys_to_delete = [key for key, value in hashset.items() if value == value_to_remove]
            answer.insert(0, keys_to_delete[0])

            for key in [keys_to_delete[0]]:
                hashset.pop(key)
            k-=1
        
        return answer

