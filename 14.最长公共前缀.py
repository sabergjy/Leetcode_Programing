class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        obj_str = ""
        for item in strs:
            if min_len >= len(item):
                 min_len = len(item)
                 obj_str = item
        #这里额可以不取最短的，取第一个元素
        
        i = 0
        all_str = ""
        for i in range(len(obj_str)):
            tag = 1
            for item in strs:
                if item[i] != obj_str[i]:
                   tag = 0
                   break
            if tag == 0:
                break
            else:
                all_str += obj_str[i]
            
        return all_str


#使用Python特性解题
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

