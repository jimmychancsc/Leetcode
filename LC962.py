import bisect
def maxWidthRamp1(A):
    stack = []
    res = 0
    for i in range(len(A))[::-1]:
        print ([A[i], i])
        if not stack or A[i] > stack[-1][0]:
            stack.append([A[i], i])
        else:
            j = stack[bisect.bisect(stack, [A[i], i])][1]
            res = max(res, j - i)
            print 'j=',j
        print "stack=",stack
        print "res=",res
    return res

def maxWidthRamp(A):
        s = []
        res = 0
        for i, a in enumerate(A):
            if not s or A[s[-1]] > a:
                s.append(i)
                print s
        for j in range(len(A))[::-1]:
            while s and A[s[-1]] <= A[j]:
                res = max(res, j - s.pop())
                print 'j=', j
                print "s=",s
                print "res=",res
        print 'j=', j
        return res

A1 = [6, 0, 8, 2, 1, 5]
A = [9,8,1,0,1,9,4,0,4,1]
print maxWidthRamp(A)