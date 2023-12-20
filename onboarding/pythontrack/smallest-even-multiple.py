class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcf(a,b):
            if a==b :
                return a
            elif a>b:
                return gcf(a-b, b)
            else:
                return gcf(a, b-a)
        def lcm(a,b):
            answer=(a*b)//gcf(a,b)
            return answer
        val=lcm(2,n)
        return val