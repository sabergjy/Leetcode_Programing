class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        #from collections import Counter
        #s = "hello-python-hello-world"
        #a = Counter(s) 可以是字符串，也可以是列表
        #print(a)
        # 结果 
        #Counter({'-': 3, 'd': 1, 'e': 2, 'h': 3, 'l': 5, 'n': 1, 'o': 4, 'p': 1, 'r': 1, 't': 1, 'w': 1, 'y': 1})
        #这个Counter是可以做对比的，用"==",只要key-val的键值对对上就行，不需要顺序
        if len(words) == 0 or len(s) == 0:
            return []
        nlength = len(words)*len(words[0])
        if len(s) < nlength:
            return [] 
        from collections import Counter
        dic_words = Counter(words) 

        res = []
        for i in range(len(s)-nlength+1):
            temp_str = s[i:i+nlength]
            temp_list = []
            for j in range(0, nlength, len(words[0])):
                temp_list.append(temp_str[j:j+len(words[0])])
            if dic_words == Counter(temp_list):
                res.append(i)
        return res
