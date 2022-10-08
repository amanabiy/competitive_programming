class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        collected -> [ "here" ]
        I will only add it to collected if it is valid ip address other wise I will just try to expand and add the next one
        
        """
        ans = set()
        
        def isValidIP(ip):
            if not ip or (len(ip) > 1 and ip[0] == "0"):
                return False
            return 0 <= int(ip) <= 255
        
        def backtrack(index, collected):
            if len(collected) == 4:
                ipAddress = '.'.join(collected)
                if len(ipAddress) == len(s) + 3:
                    ans.add(ipAddress)
                return

            for i in range(index, index + 3):
                ip = s[index: i + 1]
                if isValidIP(ip):
                    collected.append(ip)
                    backtrack(i + 1, collected)
                    collected.pop()

        backtrack(0, [])

        return ans
            
        
        