class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31-1:
            return 0
        res_num = 0
        if x <= 0:
            res_str = str(-x)
            for i in range(len(res_str)):
                res_num += 10**i*int(res_str[i])
            if -res_num < -2**31:
                return 0
            else:
                return -res_num
        else:
            res_str = str(x)
            for i in range(len(res_str)):
                res_num += 10**i*int(res_str[i])
            if res_num > 2**31-1:
                return 0
            else:
                return res_num
