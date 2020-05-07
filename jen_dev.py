import os
import webbrowser
print("""press 1: to pass
press 0: to fail
      """)
ch = int(input())
if ch == 1:
    os.system("curl --user 'akansh028:akansh@028' http://193.168.53.128:8080/job/QAT/build?token=merge")
else:
    print("not passed")

