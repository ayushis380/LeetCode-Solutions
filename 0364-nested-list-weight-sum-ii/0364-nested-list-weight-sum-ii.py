# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    # In inverse depth weighting, we instead want to give higher weight to shallower elements. One way to do this is by using: ∑(integer × ( max depth − current depth + 1))
    # M × ∑ x(i) − ∑ ( x(i) × d(i) )+ ∑ x(i)
    # ∑ x(i) is sum of elements, ∑ ( x(i) × d(i) ) is sum of products
        
        queue = deque(nestedList)
        sumOfProducts = 0
        sumOfElements = 0
        depth, maxdepth = 1, 0

        while queue:
            curlen = len(queue)
            maxdepth = max(maxdepth, depth)

            for i in range(curlen):
                val = queue.popleft()
                if val.isInteger():
                    sumOfElements += val.getInteger()
                    sumOfProducts += val.getInteger() * depth
                else:
                    queue.extend(val.getList())
            
            depth += 1
        
        return (maxdepth + 1) * sumOfElements - sumOfProducts
        