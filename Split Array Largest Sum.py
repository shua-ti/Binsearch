#-*-coding=utf-8-*-
#!/usr/bin/env python
"Split Array Largest Sum"


class Solution(object):
    def binsearch(self, nums, m, lo, hi):
        while lo < hi:
            mid = (lo + hi) // 2
            if self.valid(nums, m, mid):
                hi = mid
            else:
                lo = mid+1
        return hi

    def valid(self, nums, m, peak):
        cnt = 1
        cur = 0
        for num in nums:
            cur += num
            if cur > peak:
                cur = num
                cnt += 1
                if cnt > m:
                    return False
        return True

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        lo = max(nums)
        hi = sum(nums)
        return self.binsearch(nums, m, lo, hi)


if __name__=="__main__":
    nums =[7,2,5,10,8]
    m = 2
    inst = Solution()
    print inst.splitArray(nums,2)
