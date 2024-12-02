class FileTreeNode:
    FILE = 0
    DIR = 1

    def __init__(self, type: int, name: str, parent):
        self.type = type
        self.name = name
        self.parent = parent
        self.children = []

    def setSize(self, size):
        if not self.type == self.FILE:
            raise Exception("Tree node is not file!")
        self.size = size

    def getSize(self):
        if self.type == self.FILE:
            return self.size

        total = 0
        for c in self.children:
            total += c.getSize()

        return total

    def addChild(self, node):
        if not self.type == self.DIR:
            raise Exception("Tree node is not directory!")
        self.children.append(node)

    def navigate(self, name):
        if name == "..":
            return self.parent
        for c in self.children:
            if c.name == name:
                return c


f = open("7/input.txt")
root = FileTreeNode(FileTreeNode.DIR, "ROOT", None)
current = root
current.addChild(FileTreeNode(FileTreeNode.DIR, "/", current))

line = f.readline().strip()
while len(line) > 0:
    if line[0:4] == "$ cd":
        current = current.navigate(line[5:])
        line = f.readline().strip()
    elif line[0:4] == "$ ls":
        line = f.readline().strip()
        while len(line) > 0 and line[0] != "$":
            if line[0:3] == "dir":
                current.addChild(FileTreeNode(
                    FileTreeNode.DIR, line[4:], current))
            else:
                space = line.find(" ")
                file = FileTreeNode(FileTreeNode.FILE,
                                    line[space + 1:], current)
                file.setSize(int(line[0:space]))
                current.addChild(file)
            line = f.readline().strip()

totalSize = 70000000
available = totalSize - root.getSize()
needToClear = 30000000 - available


def iterateTree(dir):
    if dir.type == FileTreeNode.FILE:
        return None

    candidate = None
    if dir.getSize() >= needToClear:
        candidate = dir

    for c in dir.children:
        c2 = iterateTree(c)
        if c2 is not None and (candidate is None or c2.getSize() < candidate.getSize()):
            candidate = c2

    return candidate


print(needToClear)
print(iterateTree(root).name)
