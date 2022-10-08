class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        
        def isValidIP(ip):
            if not ip:
                return False
            if len(ip) > 1 and ip[0] == "0":
                return False
            if int(ip) > 255 or int(ip) < 0:
                return False
            return True
        
        ans = set()
        
        for i in range(0, 4):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    for y in range(k + 1, k + 4):
                        a, b, c, d = s[:i], s[i:j], s[j:k], s[k:y]
                        if isValidIP(a) and isValidIP(b) and isValidIP(c) and isValidIP(d):
                            v = '.'.join([a, b, c, d])
                            if len(v) == len(s) + 3:
                                ans.add(v)
        
        return ans