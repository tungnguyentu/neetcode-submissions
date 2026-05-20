class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strs:
            split = list(s)
            split.sort()
            sorted_str = ''.join(split)
            if mapping.get(sorted_str):
                mapping[sorted_str].append(s)
            else:
                mapping[sorted_str] = [s]
        return list(mapping.values())
