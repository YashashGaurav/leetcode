"""
71. Simplify Path
"""


class Solution:
    # 100.00% | 12.36%
    def simplifyPath(self, path: str) -> str:
        folder_stack = []
        components = path.split("/")

        for component in components:
            if component == "." or component == "":
                continue
            elif component == "..":
                if folder_stack:
                    folder_stack.pop()
            else:
                folder_stack.append(component)

        return "/" + "/".join(folder_stack)

    # 16.26% | 34.02%
    def simplifyPath_0(self, path: str) -> str:
        folder_stack = []
        current_folder = ""
        path = path + "/"

        for i, c in enumerate(path):
            if c == "/":
                if current_folder == "..":
                    if folder_stack:
                        folder_stack.pop()
                elif not (current_folder == "." or current_folder == ""):
                    folder_stack.append(current_folder)

                current_folder = ""

            else:
                current_folder += c

        return "/" + "/".join(folder_stack)


# Output: "/home"
print(Solution().simplifyPath(path="/home/"))

# Output: "/home/foo"
print(Solution().simplifyPath(path="/home//foo/"))

# Output: "/home/user/Pictures"
print(Solution().simplifyPath(path="/home/user/Documents/../Pictures"))

# Output: "/"
print(Solution().simplifyPath(path="/../"))

# Output: "/.../b/d"
print(Solution().simplifyPath(path="/.../a/../b/c/../d/./"))
