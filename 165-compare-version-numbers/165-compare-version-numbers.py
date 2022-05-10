class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        # v1Len = len(v1)
        # v2Len = len(v2)
        # if v1Len > v2Len:
        ans = 0
        stoped = 0
        for i in range(min(len(v1), len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v2[i]) > int(v1[i]):
                return -1
        if len(v1) > len(v2):
            for i in range(len(v2), len(v1)):
                if int(v1[i]):
                    return 1
        if len(v2) > len(v1):
            for i in range(len(v1), len(v2)):
                if int(v2[i]):
                    return -1
        return 0
                