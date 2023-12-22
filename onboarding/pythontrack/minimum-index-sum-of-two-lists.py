class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        first = defaultdict(int)
        second = defaultdict(int)
        for i, val in enumerate(list1):
            first[val] = i
        for j , value in enumerate(list2):
            second[value] = j
        ans = []
        for i in list1:
            if i in first and i in second:
                ans.append([i, first[i] + second[i]])
        ans.sort(key = lambda x: x[1])
        fin = []
        minimum = ans[0][1]
        for i in ans:
            if i[1] != minimum:
                break
            else:
                fin.append(i[0])
        return fin