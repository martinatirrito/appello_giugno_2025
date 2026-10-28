from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllYears(self):
        return DAO.getAllYears()


    # COMPONENTE CONNESSA DI DIMENSIONE MAGGIORE: STAMPARE TUTTI I NODI IN SENSO
    # DECRESCENTE DI PESO MINIMO DEGLI ARCHI INCIDENTI

    def getGraphDetails(self):
        if self._graph.number_of_edges() == 0:  # niente archi: nessun peso minimo da calcolare
            return []

        # la componente più grande (connected_components NON è ordinata per dimensione)
        connessa = max(nx.connected_components(self._graph), key=len)

        res = []
        for c in connessa:
            res.append((c, self._getMinEdge(c)))

        res.sort(key=lambda x: x[1], reverse=True)  # decrescente di peso minimo
        return res

    def _getMinEdge(self, n):
        # peso minimo tra tutti gli archi incidenti al nodo n
        return min(self._graph[n][v]['weight'] for v in self._graph.neighbors(n))

    def _getMaxEdge(self, n):
        # peso massimo tra tutti gli archi incidenti al nodo n
        return max(self._graph[n][v]['weight'] for v in self._graph.neighbors(n))