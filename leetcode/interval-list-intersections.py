class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        answer = []
        while first < len(firstList) and second < len(secondList):
            if firstList[first][0] <= secondList[second][0] or secondList[second][0] <= firstList[first][0]:
                ans = []
                if firstList[first][0] <= secondList[second][0] and firstList[first][1] >= secondList[second][0]:
                    ans.append(secondList[second][0])
                elif secondList[second][0] <= firstList[first][0] and secondList[second][1] >= firstList[first][0]:
                    ans.append(firstList[first][0])

                
                if firstList[first][1] <= secondList[second][1] and  firstList[first][1] >= secondList[second][0]:
                    ans.append(firstList[first][1])
                elif secondList[second][1] <= firstList[first][1] and secondList[second][1] >= firstList[first][0]:
                    ans.append(secondList[second][1])
                
                if len(ans) == 2:
                    answer.append(ans)

            if firstList[first][1] < secondList[second][1]:
                first += 1
            elif firstList[first][1] > secondList[second][1]:
                second +=1
            else:
                first += 1
                second += 1

        return answer