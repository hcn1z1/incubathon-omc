from core.request import AppendNewRequest
CLUBNAME = "OMC"

if __name__ == "__main__":
    print("Please Add Subject : ",end="")
    subject = input()
    print("Please Add Details (ctrl+c when u finish) : ",end ="")
    details = ""
    while True:
        try:
            details += input() + '\n'
        except:
            break
    print("\n\ndone collecting data")
    AppendNewRequest().postPendingRequests(CLUBNAME,subject,details)