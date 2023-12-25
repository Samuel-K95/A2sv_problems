class Solution:

    def check(self, s: str, d: dict):
        word = ""
        for i in s:
            word += d[i]
        return word

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        eng_alph = "abcdefghijklmnopqrstuvwxyz"
        corresponding = {}
        for i in range(26):
            corresponding[order[i]] = eng_alph[i]
        for i in range(len(words) - 1):
            if self.check(words[i], corresponding) > self.check(words[i + 1], corresponding):
                return False
        return True
        