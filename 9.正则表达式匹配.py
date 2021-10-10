#法一：动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #必须前面都放个" "字符串，不然没法处理"aab"和"c*a*b"匹配
        s = " " + s
        p = " " + p
        dp_res = [[False for i in range(len(p)+1)]for j in range(len(s)+1)] #s行，p列
        dp_res[0][0] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == ".":
                    dp_res[i+1][j+1] = dp_res[i][j]  
                
                else:#p[j]可为 "*"和其他字符
                    # s[i] 为正常字符，比如说为b,     
                    if p[j] == "*":
                        #  s = $$$b     j=xxx*
                        # p[j-1] = s[i] 或 "."
                        #另外为其他情况
                        if p[j-1] != s[i] and p[j-1] != ".":
                            dp_res[i+1][j+1] = dp_res[i+1][j-1]
                        else:
                            #此时为s = $$$b     j=xx.* /s = $$$b     j=xxb* 
                            dp_res[i+1][j+1] = dp_res[i][j+1] or dp_res[i+1][j] or dp_res[i+1][j-1]
        

                    #另外情况p[j]为其他字符,一定为false
        return dp_res[len(s)][len(p)]

#法二：正则表达式
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s1 = re.compile(p).findall(s)
        if s1 == []:
            return False
        if s1[0] == s:
            return True
        else:
            return False
