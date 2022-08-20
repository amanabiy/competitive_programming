class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for word in strs:
            k = list(word)
            k.sort()
            key = ''.join(k)
            ans[key].append(word)
            
        return ans.values()