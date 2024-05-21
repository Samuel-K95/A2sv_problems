# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        rec = set(recipes)

        graph = defaultdict(list)
        indeg = defaultdict(int)

        for idx, recipe in enumerate(recipes):
            cnt = 0
            for ing in ingredients[idx]:
                if ing not in supplies:
                    cnt += 1

                if ing in rec:
                    graph[ing].append(recipe)

            indeg[recipe] = cnt
        
        cooked = []

        queue = deque()
        vis = set()
        for i in indeg:
            if indeg[i] == 0:
                queue.append(i)
                vis.add(i)
        
        while queue:
            front = queue.popleft()

            cooked.append(front)

            for next_recipe in graph[front]:
                if next_recipe not in vis:
                    indeg[next_recipe] -= 1
                    if indeg[next_recipe]  == 0:
                        queue.append(next_recipe)
                        vis.add(next_recipe)



        return cooked



        