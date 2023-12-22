class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set(['q','w','e','r','t','y','u','i','o','p'])
        second = set(['a','s','d','f','g','h','j','k','l'])
        thrid = set(['z','x','c','v','b','n','m'])
        ans = []
        for i in range(len(words)):
            flag = True
            for j in range(len(words[i]) - 1):
                firstword, secondword = words[i][j].lower(), words[i][j+1].lower()
                if firstword in first and secondword not in first:
                    flag = False
                    break
                elif firstword in second and secondword not in second:
                    flag = False
                    break
                elif firstword in thrid and secondword not in thrid:
                    flag = False
                    break
            if flag:
                ans.append(words[i])
        return ans

        