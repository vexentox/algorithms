
"""测试题目链接：https://www.luogu.com.cn/problem/P3367"""

class Union_Find:
    """并查集类"""
    def __init__(self, n):
        """
        初始化 fa 数组
        n : 要查询点的最大编号（可以提前离散化以提高效率）
        """
        self.fa = [_ for _ in range(n)]

    def find(self, u):
        """查找 u 的根节点"""
        if u == self.fa[u]:
            return u
        self.fa[u] = self.find(self.fa[u])
        return self.fa[u]

    def merge(self, u, v):
        """合并两个节点"""
        u, v = self.find(u), self.find(v)
        if u != v:
            self.fa[u] = v

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

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
