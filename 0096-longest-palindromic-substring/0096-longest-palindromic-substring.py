class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for j in range(len(s)-i+1):
                substr = s[j:j+i]
                if substr == substr[::-1]:
                    return substr