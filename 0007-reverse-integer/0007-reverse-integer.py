MIN=-2**31
MAX=(2**31)-1
class Solution:
    def __init__(self):
        self.rev=0
        self.is_neg=False
    def reverse(self, x: int) -> int:
        if x < 0:
            self.is_neg=True
            x=abs(x)
        while(x!=0):
            digit=x%10
            x=x//10

            if self.rev > MAX//10 or (self.rev==MAX//10 and digit>MAX%10):
                return 0
            if self.rev<MIN//10 or (self.rev==MIN//10 and digit <MIN%10):
                return 0
            
            self.rev=10*self.rev+digit
        if self.is_neg:
            self.rev=-self.rev
        return self.rev
        