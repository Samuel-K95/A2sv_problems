class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tolive = timeToLive
        self.token = defaultdict(list)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = [currentTime, currentTime + self.tolive]

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token:
            expirey = self.token[tokenId][1]
            if currentTime >= expirey:
                pass
            else:
                self.token[tokenId] = [currentTime, currentTime + self.tolive]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for i in self.token:
            if self.token[i][1] > currentTime:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)