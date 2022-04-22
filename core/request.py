import pyrebase

class PendingRequests:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyCwfszX0wrK7A8dFopJIi1ZcbP3n1pBbwM",
            "authDomain": "openmindsclub-bdffa.firebaseapp.com",
            "projectId": "openmindsclub-bdffa",
            "storageBucket": "openmindsclub-bdffa.appspot.com",
            "messagingSenderId": "253658301060",
            "appId": "1:253658301060:web:100cdb337da77400f738d1",
            "measurementId": "G-HK8LD55PES",
            "databaseURL": "https://openmindsclub-bdffa-default-rtdb.firebaseio.com"
        }
        firebase = pyrebase.initialize_app(self.config)
        self.db = firebase.database()
        
    def getPendingCount(self) -> int:
        count = int(self.db.child("pending").get().val()["count"])
        return count

    def getPendingRequests(self) -> dict:
        pending = self.db.child("pending").child("new").get().val()
        return dict(pending)

    def updatePendingRequests(self,id) -> dict:
        count = self.getPendingCount()
        if count == 0: 
            raise Exception("Invalid Request")
        lastData = dict(self.db.child("pending").child("new").get().val()[id])
        self.db.child("pending").child("new").child(id).remove()
        self.db.child("pending").update({"count":f'{count-1}'}) # update count and remove from pending
        
        return lastData