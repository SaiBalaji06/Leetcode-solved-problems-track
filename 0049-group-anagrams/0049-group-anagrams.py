class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)
        for s in strs:
            k = [0] * 26
            for c in s:
                k[ord("z") - ord(c)] += 1

            ans[tuple(k)].append(s)
        
        return list(ans.values())
        

            

        