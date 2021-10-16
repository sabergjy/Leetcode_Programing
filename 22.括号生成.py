class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #用递归来做
        #深度优先遍历,一下子先遍历到底，再回溯
        #def xxx(str,left,right)
        #当左边剩余大于右边时，即不符合，要剪枝

        res_list = []
        sect_list = ["(",")"]
        def geneParent(str_,left,right):
            if left == 0 and right == 0:
                res_list.append(str_)
                return
            if left > right:
                return
            
            for item in sect_list:
                curstr = str_
                curstr += item
                if item == "(" and left > 0:
                    geneParent(curstr,left-1,right)
                elif item == ")" and right > 0:
                    geneParent(curstr,left,right-1)
        
        geneParent("",n,n)   
        return res_list