from typing import List

class Person:
    def __init__(self, name: str):
        self.name = name
        self.children = []   # List[Person]
        self.alive = True    # True if alive, False if dead

class ThroneInheritance:

    def __init__(self, kingName: str):
        # Create the root of the kingdom (the king)
        self.king = Person(kingName)
        self.personMap = {kingName: self.king}  # name -> Person object

    def birth(self, parentName: str, childName: str) -> None:
        """
        Create a new Person node and add it to the parent's children.
        """
        parent = self.personMap[parentName]
        child = Person(childName)
        parent.children.append(child)
        self.personMap[childName] = child

    def death(self, name: str) -> None:
        """
        Mark a person as dead (but keep their children intact).
        """
        person = self.personMap[name]
        person.alive = False

    def getInheritanceOrder(self) -> List[str]:
        """
        Preorder DFS traversal to return inheritance order.
        """
        order = []

        def dfs(person: Person):
            if person.alive:
                order.append(person.name)
            for child in person.children:
                dfs(child)

        dfs(self.king)
        return order
