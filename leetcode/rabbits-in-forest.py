class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        store = defaultdict(list)
        ans = 0
        for i in range(len(answers)):
            if answers[i] == 0:
                ans += 1
            else:
                if answers[i] not in store:
                    ans += (answers[i] + 1)
                    store[answers[i]].append(answers[i])
                else:
                    store[answers[i]].append(answers[i])
                    if len(store[answers[i]]) >= (answers[i] + 1):
                        del store[answers[i]]

        return ans
