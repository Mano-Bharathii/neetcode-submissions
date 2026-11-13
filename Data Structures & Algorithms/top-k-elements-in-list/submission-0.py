class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_hash = {}
        for i in nums:
            value_hash[i] = 1 + value_hash.get(i, 0)
        freq_hash = [[j, i] for i,j in value_hash.items()]
        return [i[1] for i in sorted(freq_hash)[-k:]]