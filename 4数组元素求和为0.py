class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ABsum=collections.Counter(a+b for a in A for b in B)
        count = sum(ABsum[-c-d] for c in C for d in D)
        return count
        