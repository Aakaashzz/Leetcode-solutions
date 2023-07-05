class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n==0:
                return 1
            if n<0:
                x=1/x
                n=abs(n)
            y = power(x,n//2)
            if n%2==0:
                return y*y
            return y*y*x
        y=power(x,n)
        return y