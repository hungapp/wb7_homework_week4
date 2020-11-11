class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s, stack_t = [], []
        for c in S:
            if c == '#':
                if stack_s:
                    stack_s.pop()
                continue
            stack_s.append(c)
        for c in T:
            if c == '#':
                if stack_t:
                    stack_t.pop()
                continue
            stack_t.append(c)
        return stack_s == stack_t
