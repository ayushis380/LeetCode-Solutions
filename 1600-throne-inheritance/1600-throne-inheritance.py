from collections import defaultdict
from typing import List

class ThroneInheritance:

    def __init__(self, kingName: str):
        # Initialize the king as the root of the inheritance tree
        # We track the family tree and alive status separately for efficiency.
        self.root = kingName
        self.nodeMap = defaultdict(list)  # Maps a person to their children
        self.alive = set()               # Set of living people
        self.alive.add(kingName)

    def birth(self, parentName: str, childName: str) -> None:
        """
        Add a child under the parent in the tree.
        """
        self.nodeMap[parentName].append(childName)
        self.alive.add(childName)

    def death(self, name: str) -> None:
        """
        Mark a person as dead.
        """
        if name in self.alive:
            self.alive.remove(name)

    def getInheritanceOrder(self) -> List[str]:
        """
        Perform a DFS traversal starting from the king, respecting birth order,
        and skipping over dead people.
        """
        order = []

        def dfs(person):
    # DFS adds the person before visiting children (preorder traversal), which aligns with inheritance rules.
            if person in self.alive:
                order.append(person) # Dead people are skipped, but their children can still inherit.
            for child in self.nodeMap[person]:
                dfs(child)

        dfs(self.root)
        return order
