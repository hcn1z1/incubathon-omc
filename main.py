from os import path
import sys
from threading import Timer
from threading import Thread
from img import image_rc as image_rc
from core.instagram import Instagram
from core.request import PendingRequests
from core.mailing import Sending
from core.requestsmanagement import InformationGathering
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

UIFORM,_ = loadUiType(path.join(path.dirname(__file__),"widget\\main.ui"))

class Main(QDialog,UIFORM):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # setting objects 
        self.Insta = Instagram()
        self.PRs = PendingRequests()
        self.SENDER = Sending()
        self.MANAGEMENT = InformationGathering()

        # first things that have to work / hiding some widgets and setting events for static buttons
        self.clickedButtons()
        self.hideRequests()
        self.hidePosts()
        self.hideMessages()
        self.manageInstagram()
        self.manageInformations()
        #manage application step by step
        self.currentCount = 0
        self.currentCountInsta = 0
        socialMediaPageThread = Thread(target= self.toShowOnSocialMediaPage)
        requestsPageThread = Thread(target= self.toShowOnRequestsPage)
        socialMediaPageThread.run()
        requestsPageThread.run()
        
    def manageInformations(self):
        self.count = self.PRs.getPendingCount()
        if self.count > 0:
            self.request = self.PRs.getPendingRequests()
            self.listOfIds = list(self.request.keys()) # dict keys to list 
            self.requestBtn.setText(f"REQUESTS ({self.count})")
        else:
            self.hideRequests()
            self.requestBtn.setText(f"REQUESTS (0)")
            self.showThatBackground()
    def toShowOnRequestsPage(self):
        count = self.count - self.currentCount
        if count >= 1:
            self.hideRequests()
            self.requests.show()
            idInfo = self.request[self.listOfIds[self.currentCount]]
            self.lab_request.setText(idInfo["clubname"])
            self.lb_subject.setText("Subject : " + idInfo["subject"])
            self.reqId.setText("ID : " + self.listOfIds[self.currentCount])
            self.ACCEPT.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount],self.ACCEPT))
            self.DENIED.clicked.connect(lambda: self.denyClicked(self.listOfIds[self.currentCount],self.DENIED))
        if count>=2:
            self.requests_2.show()
            idInfo = self.request[self.listOfIds[self.currentCount+1]]
            self.lab_request2.setText(idInfo["clubname"])
            self.lb_subject2.setText("Subject : " + idInfo["subject"])
            self.reqId_2.setText("ID : " + self.listOfIds[self.currentCount+1])
            self.ACCEPT_2.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount+1],self.ACCEPT_2))
            self.DENIED_3.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount],self.DENIED_3))
        if count>=3:
            self.requests_3.show()
            idInfo = self.request[self.listOfIds[self.currentCount+2]]
            self.lab_request3.setText(idInfo["clubname"])
            self.lb_subject3.setText("Subject : " + idInfo["subject"])
            self.reqId_3.setText("ID : " + self.listOfIds[self.currentCount+2])
            self.ACCEPT_3.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount+2],self.ACCEPT_3))
            self.DENIED_4.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount],self.DENIED_4))
        if count>=4:
            self.requests_4.show()
            idInfo = self.request[self.listOfIds[self.currentCount+3]]
            self.lab_request4.setText(idInfo["clubname"])
            self.lb_subject4.setText("Subject : " + idInfo["subject"])
            self.reqId_4.setText("ID : " + self.listOfIds[self.currentCount+3])
            self.ACCEPT_4.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount+3],self.ACCEPT_4))
            self.DENIED_5.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount],self.DENIED_5))
        if count>=5:
            self.requests_5.show()
            idInfo = self.request[self.listOfIds[self.currentCount+3]]
            self.lab_request5.setText(idInfo["clubname"])
            self.lb_subject5.setText("Subject : " + idInfo["subject"])
            self.reqId_5.setText("ID : " + self.listOfIds[self.currentCount+4])
            self.ACCEPT_5.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount+4],self.ACCEPT_5))
            self.DENIED_6.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount],self.DENIED_6))
        if count>=6:
            self.requests_4.show()
            idInfo = self.request[self.listOfIds[self.currentCount+3]]
            self.lab_request4.setText(idInfo["clubname"])
            self.lb_subject4.setText("Subject : " + idInfo["subject"])
            self.reqId_4.setText("ID : " + self.listOfIds[self.currentCount+5])
            self.ACCEPT_6.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount+5],self.ACCEPT_6))
            self.DENIED_7.clicked.connect(lambda: self.acceptClicked(self.listOfIds[self.currentCount],self.DENIED_7))
    
    def manageInstagram(self):
        self.countInsta = self.Insta.getCount()
        if self.countInsta > 0:
            self.posts = self.Insta.getRecent()
            self.listOfPosts = list(self.posts.keys()) # dict keys to list 
        else:
            self.hidePosts()
            self.showThatBackground()

    def toShowOnSocialMediaPage(self):
        count = self.countInsta - self.currentCountInsta
        if count >= 1:
            self.hideRequests()
            self.post.show()
            idInfo = self.posts[self.listOfPosts[self.currentCount]]
            self.postclubname.setText(idInfo["clubname"])
            self.time.setText("Time : " + idInfo["subject"])
            self.event.setText("Event : " + self.listOfPosts[self.currentCount])
            self.url.clicked.connect(lambda: self.urlButtonPressed(self.listOfPosts[self.currentCount]))
        if count>=2:
            self.post_2.show()
            idInfo = self.posts[self.listOfPosts[self.currentCount+1]]
            self.postclubname_2.setText(idInfo["clubname"])
            self.time_2.setText("Time : " + idInfo["time"])
            self.event_2.setText("Event : " + self.listOfPosts[self.currentCount+1])
            self.url_2.clicked.connect(lambda: self.urlButtonPressed(self.listOfPosts[self.currentCount+1]))
        if count>=3:
            self.post_3.show()
            idInfo = self.posts[self.listOfPosts[self.currentCount+2]]
            self.postclubname_3.setText(idInfo["clubname"])
            self.time_3.setText("Time : " + idInfo["subject"])
            self.event_3.setText("Event : " + self.listOfPosts[self.currentCount+2])
            self.url_3.clicked.connect(lambda: self.urlButtonPressed(self.listOfPosts[self.currentCount+2]))
        if count>=4:
            self.post_4.show()
            idInfo = self.posts[self.listOfPosts[self.currentCount+3]]
            self.postclubname_4.setText(idInfo["clubname"])
            self.time_4.setText("Time : " + idInfo["subject"])
            self.event_4.setText("Event : " + self.listOfPosts[self.currentCount+3])
            self.url_4.clicked.connect(lambda: self.urlButtonPressed(self.listOfPosts[self.currentCount+3]))
        if count>=5:
            self.post_5.show()
            idInfo = self.posts[self.listOfPosts[self.currentCount+3]]
            self.postclubname_5.setText(idInfo["clubname"])
            self.time_5.setText("Time : " + idInfo["subject"])
            self.event_5.setText("Event : " + self.listOfPosts[self.currentCount+4])
            self.url_5.clicked.connect(lambda: self.urlButtonPressed(self.listOfPosts[self.currentCount+4]))
        if count>=6:
            self.post_4.show()
            idInfo = self.posts[self.listOfPosts[self.currentCount+3]]
            self.postclubname_4.setText(idInfo["clubname"])
            self.time_4.setText("Time : " + idInfo["subject"])
            self.event_4.setText("ID : " + self.listOfPosts[self.currentCount+5])
            self.url_6.clicked.connect(lambda: self.urlButtonPressed(self.listOfPosts[self.currentCount+5]))

    def downArrowPressEvent(self):
        if (self.count - self.currentCount) >1 :
            self.currentCount += 1
            self.toShowOnRequestsPage()
        else:
            th = Timer(5,self.hideMessages)
            self.message.show()
            self.alert.show()
            th.start()

    def upArrowPressEvent(self):
        if (self.currentCount != 0): 
            self.currentCount -= 1
            self.toShowOnRequestsPage()
        else:
            th = Timer(5,self.hideMessages)
            self.message.show()
            self.alert.show()
            th.start()

    def hideRequests(self):
        self.requests.hide()
        self.requests_2.hide()
        self.requests_3.hide()
        self.requests_4.hide()
        self.requests_5.hide()
        self.requests_6.hide()
    
    def hidePosts(self):
        self.post.hide()
        self.post_2.hide()
        self.post_3.hide()
        self.post_4.hide()
        self.post_5.hide()

    def hideMessages(self):
        self.message.hide()
        self.alert.hide()

    def clickedButtons(self):
        self.closeBtn.clicked.connect(lambda b: self.close())
        self.minBtn.clicked.connect(lambda g: self.showMinimized())
        self.requestBtn.clicked.connect(self.firstWidget)
        self.socialMediaBtn.clicked.connect(self.secondWidget)
        self.downward.clicked.connect(self.downArrowPressEvent)
        self.upward.clicked.connect(self.upArrowPressEvent)
            
    def firstWidget(self):
        self.stackedWidget.setCurrentIndex(0)
        self.manageInformations()

    def secondWidget(self):
        self.stackedWidget.setCurrentIndex(1)
        self.manageInstagram()
    def showThatBackground(self):
        self.stackedWidget.setCurrentIndex(2)
    def acceptClicked(self,idNum,button:QPushButton):
        button.setDisabled(True)
        self.run(idNum=idNum)
        button.setDisabled(False)

    def run(self,idNum):
        th = Timer(2.3,self.manageInformations)
        task = Thread(target = self.MANAGEMENT.acceptedRequests, args=(idNum,))
        task.start()
        th.start()
        th.join()
        task.join()
    
    def denyClicked(self,idNum,button:QPushButton):
        button.setDisabled(True)
        button.setStyleSheet('''
            position: relative;
            width:10px;
            letter-spacing: 2px;
            text-decoration: none;
            text-align: center;
            color: #ffffff;
            border: 1px solid #f2f2f2;
        ''')
        self.MANAGEMENT.deniedRequests(idNum)
        th = Timer(2.3,self.manageInformations)
        th.daemon = True
        th.start()
        th.join()
        button.setDisabled(False)

    def moveWindow(self,e):
        '''
        Move Main window in any mouseEvent
        '''
        try:
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        except:
            pass

if __name__ == '__main__':
    global window

    app=QApplication(sys.argv)
    window= Main()
    window.show()
    app.exec_()