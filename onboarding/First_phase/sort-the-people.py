class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = zip(names, heights)
        pairs = sorted(pairs, key = lambda x: x[1], reverse = True)
        return [i[0] for i in pairs]
