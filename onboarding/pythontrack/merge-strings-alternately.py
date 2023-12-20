class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final= []
        count1, count2 = 0, 0
        for i in range(len(word1) + len(word2)):
            if i % 2 == 0:
                if count1 > len(word1) - 1:
                    final.append( word2[count2])
                    count2 += 1
                else:
                    final.append( word1[count1])
                    count1 += 1
            else:
                if count2 > len(word2) - 1:
                    final.append(word1[count1])
                    count1 += 1
                else:
                    final.append( word2[count2])
                    count2 += 1
        return "".join((final))
