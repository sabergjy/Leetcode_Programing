class Solution:
    def romanToInt(self, s: str) -> int:
        dic_value = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        
        res_num = 0
        i = 0
        while i < len(s):
            if i+1 < len(s):
               if s[i]+s[i+1] in dic_value:
                   res_num += dic_value[s[i]+s[i+1]]
                   i += 2
               else:
                   res_num += dic_value[s[i]]
                   i += 1
            else:
                 res_num += dic_value[s[i]]
                 i += 1
        return res_num
