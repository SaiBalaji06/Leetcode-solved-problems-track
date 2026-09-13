class Solution:
    def minWindow(self, s: str, t: str) -> str:
        req_win = {}
        curr_win = {}
        req_cnt = 0
        vaild = 0

        for ch in t:
            req_win[ch] = req_win.get(ch, 0) + 1
            req_cnt += 1
            curr_win[ch] = 0

        left = -1
        right = -1

        mnlen = float("inf")
        st = -1
        ed = -1

        while right >= left and right < len(s):
            if vaild == req_cnt:
                left += 1
                if (right - left + 1) < mnlen:
                    mnlen = right - left + 1
                    st = left
                    ed = right 
                if s[left] in curr_win:
                    curr_win[s[left]] -= 1
                    if curr_win[s[left]] < req_win[s[left]]:
                        vaild -= 1
            else:
                right += 1
                if right < len(s):
                    if s[right] in curr_win:
                        curr_win[s[right]] += 1
                        if curr_win[s[right]] <= req_win[s[right]]:
                            vaild += 1
                            
        if st == -1 and ed == -1:
            return ""
        else:
            return s[st : ed + 1]
        




         
        