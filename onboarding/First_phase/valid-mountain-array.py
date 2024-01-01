class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left = 0
        right = 1
        inc, dec = False, False
        while right < len(arr) and arr[right] > arr[left]:
            inc = True
            right += 1
            left += 1
        if right < len(arr) and arr[right] == arr[left] or (right == 1 and left == 0):
            return False
        while right < len(arr) and arr[right] < arr[left]:
            dec = True
            right += 1
            left += 1
        if right < len(arr) and arr[right] >= arr[left]:
            return False
        return True if inc and dec else False