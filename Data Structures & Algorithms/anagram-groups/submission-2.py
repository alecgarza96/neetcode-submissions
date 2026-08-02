class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        ans = {}
        for i in strs:
            s[i] = "".join(sorted(i))
        for i in strs:
            current = s.get(i)
            if ans.get(current):
                ans[current].append(i)
            else:
                ans[current] = [i]
                
        return list(ans.values())
        