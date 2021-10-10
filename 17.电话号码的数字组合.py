class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic_value = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        #用递归
        if digits == "":
            return []
        
        res_list = []

        def get_value(node,res_str):

            if node == "":
                res_list.append(res_str)
                return 
            
            for i in range(len(dic_value[node[0]])):
                temp = res_str #这里要用中间变量进行回溯
                temp += dic_value[node[0]][i]   
                get_value(node[1:], temp)
               
        get_value(digits,"")

        return res_list
