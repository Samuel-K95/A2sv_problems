class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        store = self.getRow(rowIndex - 1)
        temp = [1] * (len(store) + 1)

        for i in range(1, len(temp) - 1):
            temp[i] = store[i] + store[i-1]
        
        return temp
