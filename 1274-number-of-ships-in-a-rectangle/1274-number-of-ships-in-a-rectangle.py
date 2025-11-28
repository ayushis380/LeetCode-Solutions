# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if (bottomLeft.x > topRight.x) or (bottomLeft.y > topRight.y):
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        midx, midy = (topRight.x + bottomLeft.x)//2, (topRight.y + bottomLeft.y)//2
        
        return self.countShips(sea, Point(midx, midy), bottomLeft) + \
               self.countShips(sea, Point(topRight.x, midy), Point(midx + 1, bottomLeft.y)) + \
               self.countShips(sea, Point(midx, topRight.y), Point(bottomLeft.x, midy + 1)) + \
               self.countShips(sea, topRight, Point(midx+1, midy+1))
        