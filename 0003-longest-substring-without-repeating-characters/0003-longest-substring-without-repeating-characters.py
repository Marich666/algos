class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_symb = deque()
        max_len = 0
        for i in range(len(s)):
            if s[i] not in unique_symb:
                unique_symb.append(s[i])
            else:
                max_len = max(len(unique_symb), max_len)
                while s[i] != unique_symb[0]:
                    unique_symb.popleft()
                unique_symb.popleft()
                unique_symb.append(s[i])
        return max(max_len, len(unique_symb))
