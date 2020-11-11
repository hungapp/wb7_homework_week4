# iterative
from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = deque()
        queue.append([])
        res = []
        for cur_num in nums:
            layer_size = len(queue)
            for _ in range(layer_size):
                current = queue.popleft()
                for i in range(len(current) + 1):
                    new = list(current)
                    new.insert(i, cur_num)
                    if len(new) == len(nums):
                        res.append(new)
                    else:
                        queue.append(new)
        return  res

#recursive
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def gen_recursive(nums, index, cur):
            if len(cur) == len(nums):
                res.append(cur)
		return 
           else:
                for i in range(len(cur) + 1):
                    new = list(cur)
                    new.insert(i, nums[index])
                    gen_recursive(nums, index + 1, new)
            
        gen_recursive(nums, 0, [])
        return res


#backtrack
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def gen_recursive(nums, index, cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            else:
                for i in range(len(cur) + 1):
                    cur.insert(i, nums[index])
                    gen_recursive(nums, index + 1, cur)
                    del cur[i] #backtrack
            
        gen_recursive(nums, 0, [])
        return res
