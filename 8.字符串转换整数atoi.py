#法一：循环处理
class Solution:
    def myAtoi(self, s: str) -> int:
        #1.前面只能是空格，“0”，正负号，正常数字字符，
        #2.一旦读到除以上非数字字符，就停止转化
        setNumStr = ("1","2","3","4","5","6","7","8","9","0")
        setStartStr = ("1","2","3","4","5","6","7","8","9","0","-","+"," ")

        def strToNum(str_):
            if str_ =="+" or str_ =="-" or len(str_)==0:
                return 0
            if str_[0] == "-":
                if int(str_) < -2**31:
                    return -2**31
                else:
                    return int(str_)
            else:
                if int(str_) > 2**31-1:
                    
                    return 2**31-1
                else:   
                    return int(str_)  
        if s == "":
            return 0
        if len(s) == 1 and s not in setNumStr:
            return 0
        if s[0] not in setStartStr:
            return 0
        num_str = ""
        s = s.strip()     
        for item in s:        
            if item not in setStartStr:
                return strToNum(num_str)
            else:      
                if item in setNumStr:
                    num_str += item       
                if item == "-":
                    if len(num_str)<1:
                        num_str += "-"
                    else:
                        break
                if item == "+":
                    if len(num_str)<1:
                        num_str += "+"
                    else:
                        break
                if item == " ":
                    break
        return strToNum(num_str)

#法二正则表达式
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647    
        INT_MIN = -2147483648
        str = str.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(str)   #查找匹配的内容
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)    #返回值

#法三：有限状态机
class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        
    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans
