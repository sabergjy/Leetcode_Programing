class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #滑动窗口
        max_len = 1
        i = 0
        j = 0
        if len(s) == 0:
            return 0
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        #长度从2开始讨论
        while j < len(s)-1: 
            if s[j+1] not in s[i:j+1]:
                j += 1
                max_len = max(max_len,j-i+1)
            else:
                #需要判断和第几个重复
                i += s[i:j+1].index(s[j+1]) + 1
                j += 1
                
            
        return max_len
