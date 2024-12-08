class Solution:
    def tribonacci(self, n: int) -> int:

        if n==0:
            return 0
        elif n<=2:
            return 1
        
        t_a=0
        t_b=1
        t_c=1
        for x in range(3,n+1):
            new_t_c=t_a+t_b+t_c
            t_a,t_b,t_c=t_b,t_c,new_t_c
        return new_t_c