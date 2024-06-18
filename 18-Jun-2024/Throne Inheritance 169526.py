# Problem: Throne Inheritance - https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.deleted = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deleted.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []
        def dfs(name):
            if name not in self.deleted:
                order.append(name)
            
            for successor in self.graph[name]:
                dfs(successor)

        dfs(self.king)
        return order



        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()