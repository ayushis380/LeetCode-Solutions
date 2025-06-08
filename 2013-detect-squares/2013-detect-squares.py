class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int) # to store the count of same points, as we need count of squares formed
        self.pts = [] # to store the points

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point) # keeping a list as its easier to go through points this way, ptsCount is a map where key is a tuple

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.pts: 
            # look for diagonal of px, py, abs of x coord == abs of y coord
            # and the point shouldnt be same, a single point is not a square
            if (abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            
            # take the count of other two points, more number of points, more squares can be formed, P erms and combi of points
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)