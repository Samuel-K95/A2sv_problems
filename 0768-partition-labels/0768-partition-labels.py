class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l=0
        co=Counter()
        ch=Counter(s)
        re=[]
        eleco=0
        for r in range(len(s)):
            if s[r] not in co:
                eleco+=1
            co[s[r]]+=1
            # print(ch)
            # print(co)
            if ch[s[r]]==co[s[r]]:
                eleco-=1
            # print(eleco)
            if eleco==0:
                re.append(r-l+1)
                if r+1<len(s):
                    l=r+1
        return re


            