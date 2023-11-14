class DisjointSet:
    def __init__(self, size):
        self.vertex = [i for i in range(size)]
        self.weight = [1] * size

    def validate(self, v1):
        return 0 <= v1 < len(self.vertex)

    def size(self, v1):
        root = self.find(v1)
        return -self.vertex[root]
    
    def parent(self, v1):
        if self.vertex[v1] == v1:
          return -self.weight[v1]
        else:
          return self.vertex[v1]
        
    def isConnected(self, v1, v2):
        if not self.validate(v1) or not self.validate(v2):
            return False
        return self.find(v1) == self.find(v2)

    def find(self, v1):
        if not self.validate(v1):
            return None
        while v1 != self.vertex[v1]:
            v1 = self.vertex[v1]
        return v1

    def unionByWeight(self, v1, v2):
        if not self.validate(v1) or not self.validate(v2):
            return
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 == root2:
            return
        if self.weight[root1] > self.weight[root2]:
            self.vertex[root2] = root1
        else:
            self.vertex[root1] = root2
        self.weight[root1] += self.weight[root2]

    def unionByRank(self, v1, v2):
        if not self.validate(v1) or not self.validate(v2):
            return
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 == root2:
            return
        if self.weight[root1] < self.weight[root2]:
            self.vertex[root1] = root2
        elif self.weight[root1] > self.weight[root2]:
            self.vertex[root2] = root1
        else:
            self.vertex[root2] = root1
            self.weight[root1] += 1

    def joinBlocks(self, Connected):
        for i in range(len(Connected)):
            for j in range(len(Connected[0])):
                if Connected[i][j] == 1:
                    self.unionByWeight(i, j)

    def findBlockSets(self):
        block_sets = set()
        for i in range(len(self.vertex)):
            root = self.find(i)
            block_sets.add(root)
        return len(block_sets)

    def findBlockcount(self, blockid):
        root = self.find(blockid)
        count = self.size(root)
        return count if count > 0 else 1


if __name__ == '__main__':
    # Tasks A
    uf = DisjointSet(10)
    # 0 1-2-5-6-7 3-8-9 4
    uf.unionByRank(1, 2)
    uf.unionByRank(2, 5)
    uf.unionByRank(5, 6)
    uf.unionByWeight(6, 7)
    uf.unionByRank(3, 8)
    uf.unionByWeight(8, 9)
    print(uf.isConnected(1, 5))  # true
    print(uf.isConnected(5, 7))  # true
    print(uf.isConnected(4, 9))  # false
    # 0 1-2-5-6-7 3-8-9-4
    uf.unionByWeight(9, 4)
    print(uf.isConnected(4, 9))  # true

    # Tasks B
    Connected = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
    uf = DisjointSet(4)
    uf.joinBlocks(Connected)
    block_count = uf.findBlockcount(1)
    print("Number of blocks in the connected block set: ", block_count)

