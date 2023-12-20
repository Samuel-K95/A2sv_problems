class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            rem = n % 3
            if rem > 1:
                return False
            n //= 3
        return True