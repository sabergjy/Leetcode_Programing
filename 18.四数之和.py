class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            target_ = target  #防止不断篡改target
            if i > 0  and nums[i] == nums[i-1]:
                continue 
            target_ -= nums[i]

            #此时该题转化为三数求和
            for j in range(i+1, len(nums)-2):
                target_1 = target_
                if j > i+1 and nums[j] == nums[j-1]:
                   continue 
                target_1 -= nums[j]
                
                #转化为两数之和
                m = j + 1
                n = len(nums)-1
                while m < n:
                    if nums[m] + nums[n] == target_1:
                        if [nums[i],nums[j],nums[m],nums[n]] not in res:
                            res.append([nums[i],nums[j],nums[m],nums[n]])
                        m += 1
                        n -= 1

                    elif nums[m] + nums[n] > target_1:
                        while m < n and nums[n] == nums[n-1]:
                            n -= 1
                        n -= 1
                    else:
                        while m < n and nums[m] == nums[m + 1]:
                            m += 1
                        m += 1
        return res
