class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #法一：正则表达式
        #法二：正常寻找
        
        if needle == haystack:
            return 0
        
        if needle == "" and len(haystack) >= 1:
            return 0
        
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)-len(needle)+1):      
            if needle[0] == haystack[i]:
                if needle == haystack[i:len(needle)+i]:
                    return i
        return -1