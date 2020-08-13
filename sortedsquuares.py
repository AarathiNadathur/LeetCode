class Solution:
    def sortedSquares(self, A):
        res=[i ** 2 for i in A]
        res.sort()
        return (res)
