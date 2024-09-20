class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Create a new string for KMP processing
        new_s = s + "#" + s[::-1]
        
        # Build the KMP table
        n = len(new_s)
        lps = [0] * n  # Longest Prefix Suffix
        j = 0  # Length of previous longest prefix suffix
        
        for i in range(1, n):
            while (j > 0 and new_s[i] != new_s[j]):
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j
        
        # Length of the longest palindromic prefix
        longest_palindromic_prefix_len = lps[-1]
        
        # Characters to add in front
        to_add = s[longest_palindromic_prefix_len:][::-1]
        
        return to_add + s

            