class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def gen_combination(cur, remain, start):
            if remain == 0:
                res.append(cur[:])
                return
            for i in range(start, len(candidates)):
                if remain >= candidates[i]:
                    cur.append(candidates[i])
                    gen_combination(cur, remain - candidates[i], i)
                    cur.pop() 
                
        gen_combination([], target, 0)
        return res
    
        
        
        
