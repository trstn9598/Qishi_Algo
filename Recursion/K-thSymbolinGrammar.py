class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if K == 1:
            return 0
        if N == 1:
            return 0
        return self.kthGrammar(N-1,(K+1)//2) if (K % 2) else 1 - self.kthGrammar(N-1,K//2)
            
        
