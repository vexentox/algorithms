"""测试题目链接：https://www.luogu.com.cn/problem/P3367"""

class Union_Find:
    """并查集类"""
    def __init__(self, n):
        """
        初始化 fa 数组和 rank 数组
        n : 要查询点的最大编号（可以提前离散化以提高效率）
        """
        self.fa = [_ for _ in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, u):
        """查找 u 的根节点并进行路径分裂"""
        if u != self.fa[u]:
            self.fa[u] = self.find(self.fa[u])
        return self.fa[u]

    def merge(self, u, v):
        """按路径长度合并两个节点"""
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        if self.rank[u] < self.rank[v]:
            self.fa[u] = v
        else:
            self.fa[v] = u
            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(int(1e7))

    n, m = [int(_) for _ in input().split()]
    uf = Union_Find(n)
    for _ in range(m):
        op, x, y = [int(_) for _ in input().split()]
        if op == 1:
            uf.merge(x - 1, y - 1)
        else:
            if uf.find(x - 1) == uf.find(y - 1):
                print('Y')
            else:
                print('N')
