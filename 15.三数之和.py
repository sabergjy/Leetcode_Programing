class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  #这个排序后还是返回给自己
        
        res_num = []
        i = 0
        while i < len(nums)-2:
            #if nums[i] > 0:  这个是因为target = 0，nums[i] > 0的话后面可以不考虑了
                #break     
            if i > 0 and nums[i] == nums[i - 1]:    #已经考虑了前面的相同nums[i - 1]，后面可以不考虑了
            #如果nums[i] == nums[i+1]这样写的话，会跳过当前的i,考虑后面的i+1，会丢失情况
                i += 1
                continue            
            else:
                m = i+1
                j = len(nums)-1
                target = -nums[i]
                while m < j:
                    if nums[m] + nums[j] == -nums[i]:
                        if [nums[i],nums[m],nums[j]] not in res_num:
                            res_num.append([nums[i],nums[m],nums[j]])
                        m += 1
                        j -= 1
                    elif nums[m] + nums[j] < -nums[i]:
                        m += 1
                    
                    else:
                        j -= 1
                i += 1
        return res_num
