# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        position = defaultdict(str)
    
        splitted = s.split()
        mx = 0
        for word in splitted:
            k = int(word[-1])
            position[k] = word[:-1]
            mx = max(mx, k)

        ans = []
        for i in range(1, mx+1):
            ans.append(position[i])
        
        return " ".join(ans)


        


        