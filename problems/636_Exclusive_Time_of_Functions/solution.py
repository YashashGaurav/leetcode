"""
636. Exclusive Time of Functions
"""

from typing import List


class Solution:
    # 96.79% | 43.53%
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []  # ids
        totals = [0] * n
        last_execution_time = 0

        for log in logs:
            id, status, time = log.split(":")
            id = int(id)
            time = int(time)

            if status == "start":
                if stack:
                    # pause
                    totals[stack[-1]] += time - last_execution_time
                    # add
                stack.append(id)
                last_execution_time = time

            else:
                totals[stack.pop()] += time - last_execution_time + 1

                last_execution_time = time + 1

        return totals

    # 19.33% | 68.91%
    def exclusiveTime_0(self, n: int, logs: List[str]) -> List[int]:
        stack = []  # [id, [[time_start, time_ned], ],]
        totals = {i: 0 for i in range(n)}

        for log in logs:
            id, status, time = log.split(":")
            id = int(id)
            time = int(time)

            if status == "start":
                if stack:
                    stack[-1][1][-1].append(time)  # pause
                stack.append([id, [[time]]])

            elif stack[-1][0] == id and status == "end":
                stack[-1][1][-1].append(time + 1)
                task_id, task_times = stack.pop()
                task_total_time = 0
                for task_time in task_times:
                    task_total_time += task_time[1] - task_time[0]

                totals[task_id] += task_total_time
                # unpause
                if stack:
                    stack[-1][1].append([time + 1])

        return list(totals.values())


# [3,4]
print(Solution().exclusiveTime(n=2, logs=["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))

# [8]
print(Solution().exclusiveTime(n=1, logs=["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]))

# [7,1]
print(Solution().exclusiveTime(n=2, logs=["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]))
