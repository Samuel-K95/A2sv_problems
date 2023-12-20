class Solution:
    def freqAlphabets(self, s: str) -> str:
        alph = {
            1:'a',
            2:'b',
            3:'c',
            4:'d',
            5: 'e',
            6:'f',
            7:'g',
            8:'h',
            9:'i',
            10:'j',
            11:'k',
            12:'l',
            13:'m',
            14:'n',
            15:'o',
            16:'p',
            17:'q',
            18:'r',
            19:'s',
            20:'t',
            21:'u',
            22:'v',
            23:'w',
            24:'x',
            25:'y',
            26:'z'
        }

        ans = []
        for i in range(len(s)):
            if s[i] == '#':
                ans.pop()
                ans.pop()
                ans.append(alph[int(s[i-2:i])])
            elif s[i] != '0':
                ans.append(alph[int(s[i])])
            else:
                ans.append("-")
        return "".join(ans)