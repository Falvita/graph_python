import numpy as np
from _graph.GraphAPSP import GraphAPSP


class GraphPro(GraphAPSP):

    def __init__(self, source=[], target=[], weight=[], directed=True):
        GraphAPSP.__init__(self, source, target, weight, directed)

    @staticmethod
    def creategraph(total_nodes, pro_edges, weights, directed=True):

        source = np.array([])
        target = np.array([])
        weight = np.array([])

        for i in range(total_nodes):
            for k in range(i+1, total_nodes):
                if k == i:
                    continue

                p = 1 - pro_edges
                has_edge = np.random.choice(2, 1, p=[p, pro_edges])[0]

                if not has_edge:
                    continue

                probabilities = np.zeros(len(weights))
                probabilities = probabilities + (1 / len(weights))
                w = np.random.choice(weights, 1, p=probabilities)[0]

                source = np.append(source, i)
                target = np.append(target, k)
                weight = np.append(weight, w)

                if not directed:
                    source = np.append(source, k)
                    target = np.append(target, i)
                    weight = np.append(weight, w)

        return GraphPro(source, target, weight)


