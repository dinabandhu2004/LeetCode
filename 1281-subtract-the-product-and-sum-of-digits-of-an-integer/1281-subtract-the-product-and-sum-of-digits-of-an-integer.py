class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        add = 0
        product = 1
        while temp > 0:
            rem = temp % 10
            temp =temp // 10 
            product *= rem
            add += rem
        return product - add