# INCUBATHON Project

# Administration Management System

Developpers: Lost DevSpark !

# requirements

**python** 3.7>=

```
pyrebase4
instagrapi
openpyxl
pyqt5
```
# usage

this tool maybe runned in two forms, **executable** or **interrupted**. For executable please download *pyinstaller* and run the following code

``pyinstaller --noconsole --windowed main.py``

for interrupted the script is under name **main.py**

``python main.py``

# tech used

pyqt framework, smtplib for sending emails, pyrebase to access firebase, openpyxl to open database and writes to it.

# Add Requests to database

To do this, you should use the client program on **client/**
```
cd client/
python client.py
[add subject and details]
// press CTRL + C when you finished
```

# NOTES 
This is only a demo version. some buttons will not work such as **CALENDER** and **REPORT**.

Please Change - email@email.com - in source code in core/mailing.py by a your Email for tests purposes.

Please Don't move any file or folder and don't execute image_rc.py

The script will be well commented and documented in future versions.
