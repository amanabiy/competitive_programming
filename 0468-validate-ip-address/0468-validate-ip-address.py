class Solution:
    def validIPAddress(self, ip: str) -> str:
        
        def isValidIpv4(ip):
            if ip.startswith("0") and len(ip) > 1:
                return False
            if ip.isdigit() and 0 <= int(ip) <= 255:
                return True
            return False
        
        def isValidIpv6(ip):
            if 1 <= len(ip) <= 4:
                for i in ip:
                    if i not in 'abcdefABCDEF1234567890':
                        return False
                return True
            return False

        if ':' in ip:
            ip = ip.split(":")
            isValid = 8 == len(ip)
            for i in ip:
                isValid = isValid and isValidIpv6(i)
            return "IPv6" if isValid else "Neither"
        else:
            ip = ip.split(".")
            isValid = 4 == len(ip)
            for i in ip:
                isValid = isValid and isValidIpv4(i)
            return "IPv4" if isValid else "Neither"        
            