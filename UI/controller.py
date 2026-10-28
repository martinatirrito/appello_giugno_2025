import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleBuildGraph(self, e):
        pass


    def handlePrintDetails(self, e):

        self._view._txtGraphDetails.controls.clear()

        # grafo costruito?
        nNodi, nArchi = self._model.getNumNodesEdges()  # il metodo che restituisce (nodi, archi)
        if nNodi == 0:
            self._view.create_alert("Creare prima il grafo.")
            return

        res = self._model.getGraphDetails()  # lista di tuple (nodo, peso)
        if len(res) == 0:
            self._view._txtGraphDetails.controls.append(ft.Text("Il grafo non ha archi."))
            self._view.update_page()
            return

        self._view._txtGraphDetails.controls.append(
            ft.Text(f"Componente connessa più grande: {len(res)} nodi"))
        for nodo, peso in res:
            self._view._txtGraphDetails.controls.append(
                ft.Text(f"{nodo.name} -- peso minimo archi incidenti: {peso}"))  # A e C: "peso massimo"
        self._view.update_page()


    def handleCercaDreamChampionship(self, e):
        pass

    def fillDDYear1(self):
        anni = self._model.getAllYears()
        for a in anni:
            self._view._ddAnno1.options.append(ft.dropdown.Option(a))
        self._view.update_page()

    def fillDDYear2(self):
        anni = self._model.getAllYears()
        for a in anni:
            self._view._ddAnno2.options.append(ft.dropdown.Option(a))
        self._view.update_page()