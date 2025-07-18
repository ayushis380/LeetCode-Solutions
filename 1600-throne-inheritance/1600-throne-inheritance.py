class Person:
    def __init__(self, name):
        self.name = name
        self.dead = False
        self.children = []

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = Person(kingName)
        self.nameMap = {kingName : self.king} # name -> person

    def birth(self, parentName: str, childName: str) -> None:
        child = Person(childName)
        parent = self.nameMap[parentName]

        parent.children.append(child)
        self.nameMap[childName] = child
        

    def death(self, name: str) -> None:
        person = self.nameMap[name]
        person.dead = True

    def getInheritanceOrder(self) -> List[str]:
        root = self.king
        order = []

        def dfs(p):
            if not p.dead:
                order.append(p.name)
            for child in p.children:
                dfs(child)
        
        dfs(root)
        return order



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()