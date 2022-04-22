import pyrebase

class Instagram:
    def __init__(self) -> None:
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
    
    def getCount(self) -> int:
        count = int(self.db.child("Instagram").get().val()["count"])
        return count

    def getRecent(self) -> dict:
        instagramPostsInformations = self.db.child("Instagram").child("posts").get().val()
        return dict(instagramPostsInformations)

    def removeRecentList(self) -> None:
        self.db.child("Instagram").update({"count":"0"})
        self.db.child("Instagram").child("posts").remove()