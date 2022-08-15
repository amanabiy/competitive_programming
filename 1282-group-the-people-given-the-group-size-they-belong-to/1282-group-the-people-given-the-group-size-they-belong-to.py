class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        
        for i in range(len(groupSizes)):
            groupSizes[i] = (groupSizes[i], i)

        groupSizes.sort()
        
        for index, group in enumerate(groupSizes):
            if not ans or len(ans[-1]) >= groupSizes[index - 1][0]:
                ans.append([group[1]])
            else:
                ans[-1].append(group[1])
        
        return ans