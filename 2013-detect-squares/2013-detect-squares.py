class DetectSquares:

    def __init__(self):
        self.store = []
        self.ptMap = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.store.append(point)
        self.ptMap[(tuple(point))] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point

        for x, y in self.store:
            if (abs(x - qx) != abs(y - qy)) or x == qx or y == qy:
                continue # not a diagonal
            
            res += self.ptMap[(qx, y)] * self.ptMap[(x, qy)]

        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)