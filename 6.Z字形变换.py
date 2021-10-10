class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #3行的时候,输入PAYPALISHIRING
        #list_1 = [[P,A,Y],[A,L,I],[H,I,R],[N,G]] 
        #list_2 = [[P],[S],[I]]  放除了首尾的行
        #可以看到上下2numRows-2个元素为一组
        #输出PAHNAPLSIIGYIR

        #4行的时候,输入PAYPALISHIRING
        #list_1 = [[P,A,Y,P],[I,S,H,I],[N,G]] 
        #list_2 = [[A,L],[R,I]] 放除了首尾的行
        #输出PINALSIGYAHRPI
        #可以看到上下2numRows-2个元素为一组

        #numRows行时，list_1中的子列表为numRows个元素，list_2中的子列表为numRows-2个元素
        
        if numRows<2:
            return s
        #构建list_1和list_2
        list_s = [s[i] for i in range(len(s))]
        list_1 = []
        list_2 = []

        #group英文是组别的意思，或者一沓
        group_Nums = len(s)//(2*numRows-2)
        for i in range(group_Nums): #o(n)
            list_num1 = []
            list_num2 = []
            for j in range(numRows):
                list_num1.append(list_s.pop(0))
            list_1.append(list_num1)

            for j in range(numRows-2):
                list_num2.append(list_s.pop(0))
            list_2.append(list_num2)
        
        yu_num = len(s)%(2*numRows-2)

        if yu_num <= numRows:
            list_1.append(list_s)
        
        if numRows < yu_num < 2*numRows-2:
            list_1.append(list_s[:numRows])
            list_2.append(list_s[numRows:]+(numRows-2-len(list_s[numRows:]))*[""])
        
        #print(list_1)
        #print(list_2)
        #开始读取
        res_str = ""
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                for item in list_1:
                    if item:
                       res_str += item.pop(0)
            else:
                if len(list_1) == len(list_2):
                    for i in range(len(list_1)):
                        if list_1[i]:
                           res_str += list_1[i].pop(0)
                        if list_2[i]:
                           res_str += list_2[i].pop(-1)  
                elif len(list_1) > len(list_2):
                    for i in range(len(list_1)):
                        if i == len(list_1)-1:
                            if list_1[i]:
                               res_str += list_1[i].pop(0)
                        else:
                            if list_1[i]:
                               res_str += list_1[i].pop(0)
                            if list_2[i]:
                               res_str += list_2[i].pop(-1)  
        
        return res_str
