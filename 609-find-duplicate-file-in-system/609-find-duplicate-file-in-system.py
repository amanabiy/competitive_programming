class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        data = defaultdict(list)
        
        for path in paths:
            path = path.split()
            directory = path[0]
            for i in range(1, len(path)):
                file_name, content = path[i].split('(')
                data[content[:-1]].append(directory + '/' + file_name)

        
        return [data[key] for key in data if len(data[key]) > 1]