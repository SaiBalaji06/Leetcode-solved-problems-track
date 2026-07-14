class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 26

        mx_len = 0
        left = 0
        right = 0
        m = 0

        for right in range(n):
            freq[ord(s[right]) - ord('A')] += 1
            win = right - left + 1
            m = max(freq)
            
            while (win - m) > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
                win -= 1
                m = max(freq)

            mx_len = max(mx_len, win)
        
        return mx_len

            
            
            
        