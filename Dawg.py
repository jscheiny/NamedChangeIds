class Dawg:
    """
    Provides the functionality of a prefix retrieval tree (trie) but is more space
    optimized.
    """

    class Node:
        EOW = 'EOW'

        """
        A node in a dawg.
        """

        def __init__(self, letter):
            self.letter = letter
            self.children = {}

        def putChild(self, child):
            self.children[child.letter] = child

        def getChild(self, letter):
            return self.children[letter]

        def hasChild(self, letter):
            return letter in self.children

    def __init__(self, path):
        self.root = Dawg.Node('')
        self.eow = Dawg.Node(Dawg.Node.EOW)

        with open(path) as f:
            lines = f.readlines()
            numNodes = int(lines[0])
            nodes = [0] * numNodes
            edges = []
            lines = [l.strip().split('\t') for l in lines[1:]]
            for (i, line) in enumerate(lines):
                letter = line[0]
                if letter == 'root':
                    nodes[i] = self.root
                else:
                    nodes[i] = Dawg.Node(letter)
                for child in line[1:]:
                    if child == Dawg.Node.EOW:
                        nodes[i].putChild(self.eow)
                    else:
                        edges.append((i, int(child)))
            for (source, dest) in edges:
                nodes[source].putChild(nodes[dest])

    def _enumerate(self, prefix, root, results):
        if root.hasChild(Dawg.Node.EOW):
            results.append(prefix)
        children = root.children.items()
        children.sort()
        for (letter, child) in children:
            self._enumerate(prefix + letter, child, results)

    def enumerate(self):
        results = []
        self._enumerate('', self.root, results)
        return results