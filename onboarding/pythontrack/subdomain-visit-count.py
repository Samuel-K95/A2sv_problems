class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        collect = defaultdict(int)
        ans = []
        for i in cpdomains:
            cdom = i.split()
            count = int(cdom[0])
            dom = cdom[1].split('.')
            com = ""
            for j in range(len(dom)-1, -1, -1):
                if com == "":
                    com = dom[j]
                else:
                    com = dom[j] + "." + com
                collect[com] += count
        for key, value in collect.items():
            ans.append(str(value) + " " + key)
        return ans




        