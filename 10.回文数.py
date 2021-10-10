class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num_str = str(x)
        #如果是负数，比如-101，会把-号变为字符“-”
        
        i = 0
        j = len(num_str)-1
        while i<j:
            if num_str[i] != num_str[j]:
                return False
            else:
                i+=1
                j-=1
        
        return True
