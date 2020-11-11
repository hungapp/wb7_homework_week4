class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        # the problem becomes finding if there's a subset having sum == s // 2
        n = len(nums)
        s =  int(s / 2)
        dp = [False] * (s+1)
        
#       sum == 0 
        dp[0] = True
        for cur in nums:
            for j in range(s, cur - 1, -1):
#               if dp[j] == True, it means we can get the sum j without cur, hence we can move on to the next number else we can include cur then decide "if we have got to a valid remaining sum"
                if not dp[j] and j >= cur:
                    dp[j] = dp[j - cur]
        
        return dp[s]
