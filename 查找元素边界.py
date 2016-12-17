#!/usr/bin/env python
#-*-coding=utf-8-*-
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findrightpos(num,target,lo,hi):
            while lo < hi: 
                mid= (lo+hi) // 2
                if target < num[mid]: #[lo,mid) (mid,hi)
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        res=[-1,-1]
        leftpos=findrightpos(nums,target-1,0,len(nums))
        if leftpos==len(nums) or nums[leftpos]!=target:
            return res
        else:
            rightpos=findrightpos(nums,target,0,len(nums))
            return [leftpos,rightpos-1]

if __name__=="__main__":
    s=Solution()
    print s.searchRange([1,2,3,4,4,4,6],4)