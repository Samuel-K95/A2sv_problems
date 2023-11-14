class Solution:
    def compress(self, chars: List[str]) -> int:
        l,r=0,0
        hh=0
        while r<len(chars):
            # print(val)
            le=0
           
            while l<len(chars) and chars[l]==chars[r]:
                le+=1
                l+=1
                # print(chars)
            # print(le)
            chars[hh]=chars[r]
            hh+=1
            if le>1:
                for u in str(le):
                    chars[hh]=u
                    # l+=2
                    hh+=1
            r=l
        print(hh)
        print(chars)
        for d in range(len(chars)-hh):
            chars.pop()
        # f=0
        # while f<len(chars):
        #     # print(val)
        #     k=f+1
        #     te=chars[f]
        #     while k<len(chars) and te.isalpha() and chars[k]==te:
        #         chars.pop(k)
        #     f+=1
        #         # print(chars)
        #     # print(le)
        # return len(chars)