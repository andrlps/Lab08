import flet as ft

from model.nerc import Nerc


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()

    def handleWorstCase(self, e):
        nerc = self._view._ddNerc.value
        try:
            year = int(self._view._txtYears.value)
        except:
            year = None
        try:
            hours = int(self._view._txtHours.value)
        except:
            hours = None
        if nerc is None or year is None or hours is None:
            self._view._txtOut.controls.append(ft.Text(f"Inserire un numero per anno e numero di ore e selezionare un nerc"))
            self._view.update_page()
            return
        percorso = self._model.worstCase(nerc, year, hours)

    def fillDD(self):
        nercList = self._model.listNerc
        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v
