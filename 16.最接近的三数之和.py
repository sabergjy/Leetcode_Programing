class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  #这个排序后还是返回给自己
        min_ = 0
        min_near = float('inf')
        i = 0
        while i < len(nums)-2:
                if i > 0 and nums[i] == nums[i-1]:
                    i += 1
                    continue
                m = i+1
                j = len(nums)-1
                while m < j:
                    if target == nums[m] + nums[j] + nums[i]:
                        return target

                    if abs(nums[m] + nums[j] + nums[i] -target) < min_near:
                        min_near = abs(nums[m] + nums[j] + nums[i] -target)
                        min_ = nums[m] + nums[j] + nums[i]
                    
                    if nums[m] + nums[j] + nums[i] > target:
                        while m < j and nums[j-1] == nums[j]:
                           j -= 1
                        j -= 1
                    elif nums[m] + nums[j] + nums[i] < target:
                        while m < j and nums[m] == nums[m+1]:
                           m += 1
                        m += 1
                    
                i += 1
        return min_
