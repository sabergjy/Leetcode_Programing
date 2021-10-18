#法一：动态规划
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #动态规划定义
        #dp[i]定义为以i结尾的合法括号子串长度
        #必须存在以i为结尾的合法子串，dp[i]才大于0
        #如果以i为结尾的字符构不成合法子串，则dp[i]=0

        dp = [0 for i in range(len(s)+1)]
        
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                elif s[i-1] == ")":
                    if s[i-dp[i-1]-1] == "(" and i-dp[i-1]-1 >= 0: #i - dp[i - 1] - 1 可以为负数
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        return max(dp)


#法二，用栈
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = []           
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                   res.append(stack.pop())
                   res.append(i)
        res.sort()
        print(res)

        max_len = 0
        i = 0
        while i < len(res):
            j = i
            while j < len(res)-1:
                if res[j] + 1 == res[j+1]:
                    j += 1
                    max_len = max(max_len, j-i+1)
                else:
                    break
            i = j+1
    
        return max_len
    
#法三，用栈，不排序
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                print(stack)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                    print(stack)
                else:
                    res = max(res,i - stack[-1])
        return res