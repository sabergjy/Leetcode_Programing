class Solution:
    def isValid(self, s: str) -> bool:
        #用栈来解决
        dic_flag = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack_list = []
        for item in s:
            if item == "(" or item == "[" or item == "{":
                stack_list.append(item)
            else:
                if stack_list:
                   if dic_flag[stack_list[-1]] == item:
                       stack_list.pop(-1)
                   else:
                       return False
                else:
                   return False
        
        if stack_list:
            return False
        return True