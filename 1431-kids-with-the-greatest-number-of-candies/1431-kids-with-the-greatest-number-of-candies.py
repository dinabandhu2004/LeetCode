class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []
        largest = 0
        for i in candies:
            if i>largest:
                largest = i
        for j in candies:
            if (j+extraCandies)>=largest:
                arr.append(True)
            else:
                arr.append(False)

        return arr