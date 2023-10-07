if __name__ == '__main__':
    N = int(input())
    store=[]
    for i in range(N):
        comm = input().split()
        if comm[0] == "append":
            store.append(int(comm[1]))
        elif comm[0] == "insert":
            store.insert(int(comm[1]), int(comm[2]))
        elif comm[0] == "remove":
            store.remove(int(comm[1]))
        elif comm[0] == "sort":
            store.sort()
        elif comm[0] == "pop":
            store.pop(-1)
        elif comm[0] == "reverse":
            store.reverse()
        elif comm[0] == "print":
            print(store)