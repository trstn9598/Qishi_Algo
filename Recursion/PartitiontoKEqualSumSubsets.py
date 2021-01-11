# recursion with respect to multiple variables.
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        taken = [False] * len(nums) 
        target = total // k
        def backtrack(i, current, k_th):
            if current == target:
                if k_th == k: 
                    return True
                else:
                    return backtrack(0,0,k_th+1)
            for j in range(i, len(nums)): 
                if not taken[j] and current+nums[j] <= target:
                    taken[j] = True
                    if backtrack(j+1,current+nums[j],k_th):
                        return True
                    else:
                        taken[j] = False
                    
            return False

        return backtrack(0, 0, 1)

                    
                    
            
            
        
        
                    
                
        
        
