import sys
import doctest
import typing
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class MyNode(typing.NamedTuple):
    Node: 'Node'
    val: int = 0


class Solution:
    """
    >>> edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    >>> n = 6
    False

    """

    @staticmethod
    def mathplot(edges, n):
        G = nx.Graph()
        G.add_nodes_from(list(range(n)))
        G.add_edges_from(edges)
        ax, plot = plt.subplots(2, 2)
        subplots = plot.reshape(1, 4)[0]
        layouts = (nx.random_layout, nx.circular_layout, nx.spring_layout,
                   nx.spectral_layout)
        titles = ("Random", "Circular", "Force-Directed", "Spectral")
        for plot, layout, title in zip(subplots, layouts, titles):
            pos = layout(G)
            nx.draw_networkx(G, pos=pos, ax=plot, with_labels=True)
            plot.set_title(title)

        plt.show()

    @staticmethod
    def graphviz(edges, n):
        G = nx.Graph()
        G.add_nodes_from(list(range(n)))
        G.add_edges_from(edges)
        ax, plot = plt.subplots()
        pos = graphviz_layout(G)
        nx.draw_networkx(G, pos=pos, ax=plot, with_labels=True)
        plt.show()

    def maxDepth(self, root: 'Node') -> int:

        return 0


if __name__ == "__main__":
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    n = 6
    #Solution.graphviz(edges, n)
    #Solution.mathplot(edges, n)
    doctest.testmod()
