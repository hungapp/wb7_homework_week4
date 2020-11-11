class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(2 * val, 1)

        return stack.pop()
 
