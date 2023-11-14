n, m = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
arr1 = 0
arr2 = 0
final = []
for _ in range(n + m):
    if arr1 < len(first) and arr2 < len(second):
        if first[arr1] <= second[arr2]:
            final.append(first[arr1])
            arr1 += 1
        else:
            final.append(second[arr2])
            arr2 += 1
    else:
        if arr1 < len(first):
            final.extend(first[arr1:])
        else:
            final.extend(second[arr2:])
        break
for i in final:
    print(i, end=" ")
