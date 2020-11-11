from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        d = deque(nums)
        for _ in range(k):
            d.appendleft(d.pop())
        for i in range(len(nums)):
            nums[i] = d.popleft()
        
