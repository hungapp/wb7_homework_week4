class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range (1,n + 1)]
        self.res = []
        self.gen_combination([], 0, k, arr)
        return self.res
    
    def gen_combination(self, cur, index, target_length, arr):
        if len(cur) == target_length:
            self.res.append(cur[:])
            return
        for i in range(index, len(arr)):
            cur.append(arr[i])
            self.gen_combination(cur, i + 1, target_length, arr)
            cur.pop() #backtrack
            
