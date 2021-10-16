class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #快慢指针
        #从第一个开始考虑
        #如果相同，快指针增加，
        #如果不同，快慢指针才同时增加

        if nums == []:
            return 0
        
        fast = 1
        slow = 1
        while fast < len(nums):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow