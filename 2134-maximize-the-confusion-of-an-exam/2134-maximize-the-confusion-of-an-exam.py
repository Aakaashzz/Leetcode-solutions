class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i,j,op1=0,0,float('-inf')
        n=len(answerKey)
        cnt=0

        while j<n:
            if answerKey[j]=='F':
                cnt+=1
            if cnt>k:
                while cnt>k:
                    if answerKey[i]=='F':
                        cnt-=1
                    i+=1
            op1=max(op1,(j-i)+1)
            j+=1
        Tcnt=0
        i,j,op2=0,0,float('-inf')
        op2=float('-inf')
        while j<n:
            if answerKey[j]=='T':
                Tcnt+=1
            if Tcnt>k:
                while Tcnt>k:
                    if answerKey[i]=='T':
                        Tcnt-=1
                    i+=1
            op2=max(op2,(j-i)+1)
            j+=1
        return max(op1,op2)