class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        all = {}
        for i in cpdomains:
            store = i.split(" ")
            dom = len(store[1]) - 1
            while dom > 0:
                if store[1][dom] == ".":
                    try:
                        all[store[1][dom + 1 :]] += int(store[0])
                    except:
                        all[store[1][dom + 1 :]] = int(store[0])
                dom -= 1
            try:
                all[store[1]] += int(store[0])
            except:
                all[store[1]] = int(store[0])
            ans = []
        for key, values in all.items():
            ans.append(str(values) + " " + key)
        return ans


cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
ans = Solution()
print(ans.subdomainVisits(cpdomains))
