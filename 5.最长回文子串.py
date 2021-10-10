class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #def IsPalindromic(str_): #o(n)
            #i = 0
            #j = len(str_)-1
            #if len(str_) == 0:
                #return False
            #if len(str_) == 1:
                #return True
                
            #while i <= j:
                #if str_[i] == str_[j]:
                    #i += 1
                    #j -= 1
                #else:
                    #return False
            #return True
        
        if len(s) < 2:
            return s
        
        dp_list = [[False for i in range(len(s))] for j in range(len(s))]  #二维数组表达式

        for i in range(len(s)):
            dp_list[i][i] = True
        
        #1.当长度为小于等于3的子串时(j-i+1<=3)，只要s[i] = s[j] 那么就是回文串
        #2.dp[i][j]是左闭右闭区间
        #3.因为是子串，所以只考虑列表斜上角的元素，因为j>=i
        #4.状态转移方程：dp_list[i][j] = dp_list[i+1][j-1]
        max_len = 1
        begin = 0
        for j in range(1,len(s)):
            for i in range(j+1): #o(n*n)
                if s[i] != s[j]:
                    dp_list[i][j] = False
                else:
                    if j-i < 3:
                        dp_list[i][j] = True
                    else:
                        dp_list[i][j] = dp_list[i+1][j-1]
                if dp_list[i][j] and j-i+1>=max_len:
                    max_len = j-i+1
                    begin = i

        return s[begin:begin + max_len]