class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            operation = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    operation += abs(j - i)
            ans.append(operation)
        return ans

        