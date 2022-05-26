

import os
import datetime
y = datetime.datetime.now()
os.system("python time-generator.py")
x = f"git commit -m \"Last Updated ON:{y}\""
os.system("git add .")
os.system(x)
os.system("git push -u origin master")
