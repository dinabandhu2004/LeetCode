class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c**.5)

        while a<=b:
            sum = a*a + b*b

            if sum == c:
                return True
            if sum<c:
                a+=1
            if sum>c:
                b-=1

        return False