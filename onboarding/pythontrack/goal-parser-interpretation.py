class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        for left in range(len(command)):
            if command[left] == 'G':
                ans.append('G')
            else:
                if command[left] == '(':
                    right = left + 1
                    ins = ""
                    while command[right] != ')':
                        ins += command[right]
                        right += 1
                    if ins == "":
                        ans.append('o')
                    else:
                        ans.append(ins)
                left = right
        return "".join(ans)
        