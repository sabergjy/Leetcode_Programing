class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        if dividend == - 2**31 and divisor == -1:
            return 2**31-1
        
        #开始递归 (位运算)
        #(60-32)/8 + 4 = (60-32-16)/8 +4 +2 =(60-32-16-8)/8 +4 +2 + 1
        ##(60-8)/8 + 1 = (60-8-16)/8 +1 +2 =(60-8-16-32)/8 +2 + 1+ 4
        #100-3-6-12-24-48 -3-3
        if dividend > 0 and divisor > 0:
            tag = 1
        if dividend < 0 and divisor > 0:
            tag = -1
        if dividend > 0 and divisor < 0:
            tag = -1
        if dividend < 0 and divisor < 0:
            tag = 1
        
        def div(n, m, t):
            if n < m :
                return 0
            if n >= m and n < t*m:
                return div(n, m, 1)    
            n -= t*m
            return t + div(n, m, 2*t)
        
        return tag*div(abs(dividend), abs(divisor), 1)