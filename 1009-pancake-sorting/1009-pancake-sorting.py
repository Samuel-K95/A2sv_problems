class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        min_ = 1
        max_ = len(arr)
        re = []
        if arr[0] == max_ or arr[max_ - 1] == min_:
            arr.reverse()
            re.append(max_)
        r = max_
        while arr != sorted(arr):
            ind = arr.index(max(arr[:r]))
            re.append(ind + 1)
            if ind!=0:arr[: ind + 1] = arr[: ind + 1][::-1]
            arr[:r] = arr[:r][::-1]
            re.append(r)
            r -= 1
        return re