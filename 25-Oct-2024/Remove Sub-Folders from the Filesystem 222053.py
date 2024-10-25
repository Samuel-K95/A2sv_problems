# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders = {}
        folder.sort(key=lambda x:len(x))

        ans = []
        for sub in folder:
            sub = sub.split('/')
            flag = True
            curr = ['/']
            for i in range(len(sub)):
                chunk = sub[i]
                if chunk:
                    curr.append(chunk)
                if "".join(curr) in folders:
                    flag = False
                    break
                if i != len(sub)-1 and i != 0:
                    curr.append('/')
            if flag:
                folders["".join(curr)] = 1
                ans.append("".join(curr))

        return ans

