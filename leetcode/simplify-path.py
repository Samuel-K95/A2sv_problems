class Solution:
    def simplifyPath(self, path: str) -> str:
        listpath = path.split('/')
        store = []
        for i in range(len(listpath)):
            if listpath[i] == '..' and store:
                store.pop()
            elif listpath[i] != '.' and listpath[i] != "" and listpath[i] != '..':
                store.append("/" + listpath[i])
        return "".join(store) if len(store) > 0 else "/"