class Solution:
    def maxArea(self, height: List[int]) -> int:
        #使用双指针滑动窗口
        #首先要认清两点：
        #1.双指针，一个再数组最左边，一个在最右边，这样滑动的时候，可以囊括所有情况
        #2.移动小的一边指针，因为只有移动小的一边，才能得到比当前更大的容量。（移动大的一边，一定比之前的容量小）
        #这样一定能遇到最大容量

        #粗暴的方法，双循环 o(n**2)
        #滑动窗口，o(n)
        if len(height) == 1:
            return 0
        i = 0
        j = len(height)-1

        max_area = 0
        while i < j:
            max_area = max(max_area, (j-i)*min(height[i],height[j]))
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return max_area
