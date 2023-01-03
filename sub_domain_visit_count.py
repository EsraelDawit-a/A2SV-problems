class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_map = {}
        for domain in cpdomains:
            count,sub_domain = domain.split()
            sub_domain = sub_domain.split(".")
            for i in range(len(sub_domain)):
                target_domain = (".".join(sub_domain[i:]))
                hash_map[target_domain] = hash_map.get(target_domain,0)+int(count)
        result = [f"{hash_map[key]} {key}" for key in hash_map.keys()]
        return result
