class Solution:
    def intToRoman(self, num: int) -> str:
        value_table = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")]
        
        res_list = []
        for item in value_table:
            if num >= item[0]:
                while num >= item[0]:
                    res_list.append(item[1])
                    num -= item[0]
            if num == 0:
                break
        return "".join(res_list)


#不能用字典！！！

