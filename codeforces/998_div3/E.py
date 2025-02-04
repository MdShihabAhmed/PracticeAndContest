import sys

class DisjointSets:
    def __init__(self, size: int) -> None:
        self.parents = [i for i in range(size)]
        self.sizes = [1 for _ in range(size)]
        self.num = size

    def __len__(self):
        return self.num

    def find(self, x: int) -> int:
        """:return: the "representative" node in x's component"""
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self, x: int, y: int) -> bool:
        """:return: whether the merge changed connectivity"""
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False

        if self.sizes[x_root] < self.sizes[y_root]:
            x_root, y_root = y_root, x_root

        self.parents[y_root] = x_root
        self.sizes[x_root] += self.sizes[y_root]
        self.num-=1
        return True

    def connected(self, x: int, y: int) -> bool:
        """:return: whether x and y are in the same connected component"""
        return self.find(x) == self.find(y)

input = sys.stdin.readline

for _ in range(int(input())):
    n, m1, m2 = map(int,input().split())
    f = DisjointSets(n)
    g = DisjointSets(n)

    edges1 =[]
    for i in range(m1):
        u, v = map(int,input().split())
        u-=1
        v-=1
        edges1.append([u,v])
    
    edges2 =[]
    for i in range(m2):
        u, v = map(int,input().split())
        u-=1
        v-=1
        g.unite(u,v)
    
    result = 0
    for i in range(m1):
        x, y = edges1[i]
        if g.connected(x,y):
            f.unite(x,y)
        else:
            result+=1
    result+=(len(f)-len(g))
    print(result)
