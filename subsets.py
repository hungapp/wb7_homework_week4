class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start_index = 0, current = []):
            if len(current) == k:
                output.append(current[:]) #make a copy of current cause current will be used in the next iteration
            for i in range(start_index, n):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop() #backtrack so that it can append another number to the same index in the next iteration
        
        output = []
        n = len(nums)
#       find sets having length k
        for k in range(n + 1):
            backtrack()
        return output
