
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        if len(nums) <= 1:
            return []
        dict_res = {}
        for k,v in enumerate(nums):
            dict_res[v] = k
        for i,num in enumerate(nums):
        #通过字典get的方法来寻找，运用哈希表的原理，时间复杂度在o(1)
            if dict_res.get(target - num) and i != dict_res.get(target - num):
                res.append(i)
                res.append(dict_res.get(target - num))
                break
        return res

print(twoSum([2,3,1,3,4,5],8))



