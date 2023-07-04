class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        x = {}
        for i in range(0,10):
            x[str(i)] = i
        i1 = []
        i2 = []
        mul = 10
        for i,j in enumerate(num1[::-1]):
            i1.append(x[j] * (mul**i))
        for i,j in enumerate(num2[::-1]):
            i2.append(x[j] * (mul**i)) 
        return (str(sum(i1)*sum(i2))) 
        