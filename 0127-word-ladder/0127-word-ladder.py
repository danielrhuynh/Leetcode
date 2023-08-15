class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Making adj list
        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            # Get every pattern
            for j in range(len(word)):
                # Make pattern
                pattern = word[:j] + "*" + word[j+1:]
                adj[pattern].append(word)
        
        # BFS
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            # go through current layer
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighWord in adj[pattern]:
                        if neighWord not in visited:
                            q.append(neighWord)
                            visited.add(neighWord)
            res += 1
        return 0
        
        