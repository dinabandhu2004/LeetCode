class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        count= 0
        while temp>0:
            rem = temp%10
            if num % rem == 0:
                count+=1
            temp = temp //10
        return count
        # using for loop
        # temp = str(num)
        # count= 0
        # for i in range(len(temp)):
        #     if num %int(temp[i])==0:
        #         count +=1
        # return count