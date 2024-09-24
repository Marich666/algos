class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for word in strs:
            mapping[''.join(sorted(word))].append(word)

        return list(mapping.values())
