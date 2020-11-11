class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def gen_paren(curr = '', left = 0, right = 0):
            if len(curr) == n * 2:
                res.append(curr)
                return
            if left < n:
                gen_paren(curr + '(', left + 1, right)
            if right < left:
                gen_paren(curr + ')', left, right + 1)
        
        gen_paren()
        return res
