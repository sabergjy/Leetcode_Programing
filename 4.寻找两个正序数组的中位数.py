class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #先合并，再取中位数
        def getMiddenNumber(num_list):
            if len(num_list)%2:
                return num_list[len(num_list)//2]
        
            if len(num_list)%2 == 0:
                return (num_list[len(num_list)//2-1]+num_list[len(num_list)//2])/2
       
        res_num = []
        
        i = 0 #nums1
        j = 0 #nums2
        
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if len(nums1) == 0 and len(nums2) != 0:
            return getMiddenNumber(nums2)
        if len(nums1) != 0 and len(nums2) == 0:
            return getMiddenNumber(nums1)


        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res_num.append(nums1[i])
                i += 1
            else:
                res_num.append(nums2[j])
                j += 1
            
        if i == len(nums1) and j < len(nums2):
            res_num += nums2[j:]

        if j == len(nums2) and i < len(nums1):
            res_num += nums1[i:]

        #%取余数
        #//取整除法
        #/浮点除法
        return getMiddenNumber(res_num)