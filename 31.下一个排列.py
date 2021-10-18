class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #reverse = True 降序， reverse = False 升序（默认）
        if len(nums) == 1:
            return nums
        
        #思路：找一个较小的数和较大的数，然后交换这两个数（保证下一个序列比当前的大），再对较大数右边的序列升序排列
        #较小的数和较大的数满足两个条件：
        #1.较小的数尽量靠右，同时较大的数一定在较小的数右边   ->所以要从后向前找
        #2.较大的数比较小的数大的同时，要尽可能的小


        #以排列 [4,5,2,6,3,1]为例：
        #我们能找到的符合条件的一对「较小数」与「较大数」的组合为 22 与 33，满足「较小数」尽量靠右，而「较大数」尽可能小。
        #当我们完成交换后排列变为 [4,5,3,6,2,1]，此时我们可以重排「较小数」右边的序列，序列变为 [4,5,3,1,2,6]。


        #首先从后向前查找第一个顺序对 (i,i+1)，满足 a[i] < a[i+1]。这样「较小数」即为 a[i]。此时 [i+1,n) 必然是下降序列。
        #如果找到了顺序对，那么在区间 [i+1,n) 中从后向前查找第一个元素 j 满足 a[i]<a[j]。这样「较大数」即为 a[j]。
        #交换 a[i] 与 a[j]，此时可以证明区间[i+1,n) 必为降序。我们可以直接使用双指针反转区间 [i+1,n) 使其变为升序，而无需对该区间进行排序。

        
        n = len(nums)

        for i in range(n-2,-1,-1):
            if i == 0 and nums[i] >= nums[i+1]:
                return nums.sort()
            if nums[i] < nums[i+1]:
                for j in range(n-1,i,-1):
                    if nums[i] < nums[j]:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
                break
            
        nums[i+1:] = reversed(nums[i+1:])
        return nums