"""
    1152. Analyze User Website Visit Pattern
"""

from collections import defaultdict
from typing import List


# best I could understand ugh
class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:

        d = defaultdict(lambda: {})

        # create sorted tuple dictionary
        for i in range(len(username)):
            d[username[i]][timestamp[i]] = website[i]

        pattern_tracker_dict = {}

        for user, time_dict in d.items():
            if len(time_dict) >= 3:
                od_timestamps = sorted(list(time_dict.keys()))
                for idx in range(len(od_timestamps) - 2):
                    pattern_tracker_dict.setdefault(
                        (
                            time_dict[od_timestamps[idx]],
                            time_dict[od_timestamps[idx + 1]],
                            time_dict[od_timestamps[idx + 2]],
                        ),
                        0,
                    )
                    pattern_tracker_dict[
                        (
                            time_dict[od_timestamps[idx]],
                            time_dict[od_timestamps[idx + 1]],
                            time_dict[od_timestamps[idx + 2]],
                        )
                    ] += 1

        max_keys = [
            key
            for key, value in pattern_tracker_dict.items()
            if value == max(pattern_tracker_dict.values())
        ]

        return sorted(max_keys)[0]


def test_solution():
    # test 1
    username = [
        "joe",
        "joe",
        "joe",
        "james",
        "james",
        "james",
        "james",
        "mary",
        "mary",
        "mary",
    ]
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website = [
        "home",
        "about",
        "career",
        "home",
        "cart",
        "maps",
        "home",
        "home",
        "about",
        "career",
    ]
    # ["home","about","career"]
    print(Solution().mostVisitedPattern(username, timestamp, website))

    username = ["ua", "ua", "ua", "ub", "ub", "ub"]
    timestamp = [1, 2, 3, 4, 5, 6]
    website = ["a", "b", "a", "a", "b", "c"]

    print(Solution().mostVisitedPattern(username, timestamp, website))

    username = ["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
    timestamp = [436363475,710406388,386655081,797150921]
    website = ["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]

    print(Solution().mostVisitedPattern(username, timestamp, website))


test_solution()
