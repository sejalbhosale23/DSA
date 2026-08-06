class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """

        from collections import defaultdict, deque

        # Create graph
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods using BFS
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                if nei not in suspicious:
                    suspicious.add(nei)
                    queue.append(nei)

        # Check whether any non-suspicious method calls a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # Remove suspicious methods
        ans = []

        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans