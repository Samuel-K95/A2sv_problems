class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def check(ele,ch):
            eleCount=Counter(ele)
            for k in eleCount:
                if eleCount[k]!=ch[k]:
                    return False
            return True
        result=[]
        window=[]
        cou=Counter(s)
        for i in s:
            window.append(i)
            if check(window,cou):
                result.append(len(window))
                window=[]
        return result
            