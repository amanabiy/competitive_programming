class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        foods = defaultdict(list)
        visited = defaultdict(int)
        ans = []

        for i in range(len(recipes)):
            foods[recipes[i]] = ingredients[i]
        receeep = set(recipes)
        def dfs(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False
            if node not in supplies and not foods[node]:
                return True
            visited[node] = 1
            for ingredient in foods[node]:
                if dfs(ingredient):
                    return True

            visited[node] = 2
            if node in receeep:
                ans.append(node)
            return False
        
        
        for i in range(len(recipes)):
            if not visited[recipes[i]]:
                dfs(recipes[i])
            
        return ans