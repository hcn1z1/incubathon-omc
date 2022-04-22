from core.request import PendingRequests
from core.mailing import Sending
from openpyxl import load_workbook

class InformationGathering(PendingRequests):
    def __init__(self) -> None:
        PendingRequests.__init__(self)
        self.database = load_workbook("database/db.xlsx")
        self.configuration = self.database.active
        self.configuration.title = "Requests database"

    def acceptedRequests(self,ID):
        lastData = self.updatePendingRequests(ID)
        self.configuration.append([lastData["clubname"],ID,lastData["subject"],"ACCEPTED"])
        self.database.save("database/db.xlsx")
        Sending().acceptance(ID,"mohamedevander@gmail.com",lastData["clubname"],lastData["subject"])

    def deniedRequests(self,ID):
        lastData = self.updatePendingRequests(ID)
        self.configuration.append([lastData["clubname"],ID,lastData["subject"],"DENIED"])
        self.database.save("database/db.xlsx")
        Sending().denial(ID,"mohamedevander@gmail.com",lastData["clubname"],lastData["subject"])