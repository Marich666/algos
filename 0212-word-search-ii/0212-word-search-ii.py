class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["*"] = "*"

    def delete(self, word: str) -> bool:
        def _delete(node, word, depth):
            if depth == len(word):
                del node["*"]
                return len(node) == 0

            char = word[depth]
            if char not in node:
                return False

            should_delete_child = _delete(node[char], word, depth + 1)

            if should_delete_child:
                del node[char]
                return len(node) == 0
            return False

        return _delete(self.trie, word, 0)

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        rows, cols = len(board), len(board[0])
        visit = set()
        res = []

        def dfs(r, c, nodes, word):
            if rows<=r or r<0 or cols<=c or c<0 or (board[r][c] not in nodes) or (r, c) in visit:
                return
            visit.add((r, c))
            word += board[r][c]
            nodes = nodes[board[r][c]]
            if "*" in nodes:
                res.append(word)
                trie.delete(word)
            dfs(r + 1, c, nodes, word)
            dfs(r - 1, c, nodes, word)
            dfs(r, c + 1, nodes, word)
            dfs(r, c - 1, nodes, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                nodes = trie.trie
                dfs(r, c, nodes, "")
        return res