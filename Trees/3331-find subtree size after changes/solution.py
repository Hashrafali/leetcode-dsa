import sys
sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent, s):

        n = len(parent)

        # Step 1: Build the original tree
        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        # Step 2: Find the new parent of each node
        new_parent = parent[:]

        # last[0] = latest 'a' ancestor
        # last[1] = latest 'b' ancestor
        # ...
        last = [-1] * 26

        def dfs(node):

            # Convert character to number
            # a -> 0, b -> 1, c -> 2 ...
            ch = ord(s[node]) - ord('a')

            # Remember previous same-character ancestor
            old = last[ch]

            # If same character ancestor exists
            if old != -1:
                new_parent[node] = old

            # Current node becomes latest ancestor
            last[ch] = node

            # Visit children
            for child in tree[node]:
                dfs(child)

            # Go back to previous ancestor
            last[ch] = old

        dfs(0)

        # Step 3: Build the changed tree
        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[new_parent[i]].append(i)

        # Step 4: Find subtree sizes
        answer = [1] * n

        def find_size(node):

            for child in tree[node]:
                find_size(child)

                answer[node] += answer[child]

        find_size(0)

        return answer
