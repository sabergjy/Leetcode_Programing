class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #二分法
        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)
        l = 0

        r = len(nums)
        
        while l < r:
            mid = (l+r)//2
            if target == nums[mid]:
                print(mid)
                return mid
            elif target < nums[mid]:
                r = mid
            
            else:
                l = mid+1
        if l == r and nums[r] < target:
            return r+1

        if l == r and nums[r] > target:
            return r
        
        if l > r:
            return r+1