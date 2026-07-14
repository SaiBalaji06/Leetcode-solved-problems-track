class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s) - 1
        freq = [0] * 26

        mx_len = 0
        left = 0
        right = 0
        m = 0

        while right <= n:
            freq[ord('Z') - ord(s[right])] += 1
            m = max(m, freq[ord('Z') - ord(s[right])])
            
            while ((right - left + 1) - m) > k:
                freq[ord('Z') - ord(s[left])] -= 1
                left += 1
                m = max(freq)

            mx_len = max(mx_len, (right - left + 1))
            right += 1 
        
        return mx_len

            
            
            
        