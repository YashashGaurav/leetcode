"""
721. Accounts Merge
"""

from collections import defaultdict
from typing import List


class Solution:
    # 5.98% | 5.07%
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = defaultdict(lambda: [])

        for acc_id, account in enumerate(accounts):
            for email in account[1:]:
                email_to_id[email].append(acc_id)

        adj = defaultdict(lambda: set())

        for acc_id, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    for id in email_to_id[email]:
                        if id != acc_id:
                            adj[acc_id].add(id)

        visited = set()

        def dfs(acc_id: int):
            if acc_id in visited:
                return set()

            visited.add(acc_id)

            child_emails = set()
            for adj_id in adj[acc_id]:
                child_emails.update(dfs(adj_id))

            emails = set()
            emails.update(accounts[acc_id][1:])
            emails.update(child_emails)
            return emails

        res = []
        for acc_id, account in enumerate(accounts):
            if acc_id not in visited:
                name = [accounts[acc_id][0]]
                emails = sorted(list(dfs(acc_id)))

                res.append(name + emails)

        return res


# Output: [
#   ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
#   ["Mary","mary@mail.com"],
#   ["John","johnnybravo@mail.com"]
# ]
print(
    Solution().accountsMerge(
        accounts=[
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
    )
)

# Output: [
#   ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
#   ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
#   ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
#   ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
#   ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]
# ]
print(
    Solution().accountsMerge(
        accounts=[
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ]
    )
)
