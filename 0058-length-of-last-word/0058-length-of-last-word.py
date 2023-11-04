class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        for i in words[::-1]:
            if i != "":
                return len(i)