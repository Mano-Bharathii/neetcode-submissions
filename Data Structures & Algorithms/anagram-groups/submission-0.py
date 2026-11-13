class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in hash:
                hash[key].append(i)
            else:
                hash[key] = [i]
        return list(hash.values())





