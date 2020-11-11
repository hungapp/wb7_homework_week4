class Solution: 
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_dict = {}
        stack = []
        for n in nums2:
#           keep appedning n into the stack until n > stack[-1]
            while stack and stack[-1] < n:
                top = stack.pop()
                greater_dict[top] = n
            stack.append(n)
        return [greater_dict.get(n, -1) for n in nums1]
