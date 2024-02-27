class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
            
        def pascal (arr, n,k):
            if n == 0:
                arr = [1]
            if n == 1:
                arr = [1, 1]
            if n == k+1:
                return arr
            temp = [1] * (n + 1)
            for i in range(1, len(temp)-1):
                temp[i] = arr[i-1] + arr[i]
            return pascal(temp, n + 1, k)

        return pascal([], 0, rowIndex)
        