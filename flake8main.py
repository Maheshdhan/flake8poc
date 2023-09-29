


import os
import time
from flake8.api import legacy as flake8


codeString="print('hello')\nfor module in activeAlarms:  \n    print(module)"

parsedCode=codeString.strip("\'")

fileName="module1.py"
if os.path.exists(fileName):
  os.remove(fileName)
else:
  print("The file does not exist")
f = open(fileName, "x")
f.write(parsedCode)
f.close()


def checkLinting():
    ignore=['W2',]
    # builtins=['activeAlrms']
    # f=open('setup.cfg','w')
    # f.write('[flake8]\nignore=E5,E2,E1,E3,W2\ndisable_noqa = true')
    # f.write('\nbuiltins = activeAlarms,')
    # f.close
    
    
    style_guide = flake8.get_style_guide(
      ignore=['W2'],
      builtins=['activeAlarms']
    
      )
    # style_guide = flake8.get_style_guide(config_file='setup.cfg')
    report = style_guide.check_files([fileName])
    error=report.get_statistics('E')
    fmsg=report.get_statistics('F')
    errorMessages=error+fmsg
    # assert report.get_statistics('E') == [], 'Flake8 found violations'
    print(errorMessages) 
    # print(errorMessages[:1])   

checkLinting()

