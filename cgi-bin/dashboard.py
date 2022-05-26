#!/usr/bin/python3
import time
import cgi, cgitb
import os
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
time = str(dt_string)
#theme_detect
client_ip = os.environ["REMOTE_ADDR"]
client_ip = str(client_ip)
with open("log.txt", "a") as logger:
    logger.write(time + client_ip + ">  accessed the dashboard\n")
    logger.close()

theme = open("theme.conf", "r").read()

#if theme not in ["mint", "default"]:
#    theme = "default.css"
#elif client_ip.endswith("121") or client_ip.endswith("111"):
#    theme = "mint.css"
#else:
#    theme = theme + ".css"
theme = theme + ".css"
with open("output.txt", "w") as re:
    re.write("")
    re.close()
command = "neofetch --stdout > output.txt"
os.system(command)
print("")
print(f"""
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="20">


    <link rel="stylesheet" href="/{theme}" type="text/css">
    <title>Ourserver-Dashboard</title>
<link rel="shortcut icon" type="image/png" href="/files/favicon.png">
<!meta name="viewport" content="width=device-width, initial-scale=1">
</head><hr>
<br><br>
<a href="http://192.168.0.103" target="_blank">Ourserver</a>
<a href="http://192.168.0.103:9909/" target="_blank">Study-Server</a>

<a href="http://192.168.0.103:32400/web" target="_blank">Media Server</a>
<br><br><a href="http://192.168.0.103:9099/cgi-bin/dashboard.py" target="_blank">Server Status</a>

<a href="http://192.168.0.103:9011/"target="_blank">Typing Test</a>
 <a href="http://192.168.0.103/resource/college_routine/college_routine.jpg" target="_blank">College Routine</a>

<br><br><br><br>
<hr>
<a href="http://192.168.0.103/Share/studyplan/shagato/studyplan.html" target="_blank">Study Plan - Shagato</a>

<hr>
<br><br>
<a href="http://192.168.0.103/Subjects/Biology/" target="_blank">Biology</a>

<a href="http://192.168.0.103/Subjects/Chemistry/" target="_blank">Chemistry</a>


<a href="http://192.168.0.103/Subjects/HigherMath/" target="_blank">Highermath</a>


<a href="http://192.168.0.103/Subjects/Physics/" target="_blank">Physics</a>
<br><br><hr>
<br><br>
<a href="http://192.168.0.103/ShortSyllabus/" target="_blank">Short Syllabus</a>

<a href="http://192.168.0.103/resource/hsc/" target="_blank">All 10 Min Classes</a>
<a href="https://aparsclassroom.com/BngEngICT/" target="_blank">BAN & ENG & ICT</a>
<a href="https://cuetscctg.edu.bd/notices/" target="_blank">College Notice</a>
<br><br><hr>

""")

text1 = open("output.txt", "r").read().splitlines()
uptime_string = text1[4]

wo_uptime = uptime_string[7:]

wo_uptime = wo_uptime.replace(",", "")
uptime_string = """<br><br><p id="uptime"><span id="uptime_title">#System Up Time:</span>{}</p>
""".format(wo_uptime)

print(uptime_string)
print("")
log_size = os.path.getsize('log.txt') 
log_size = int(log_size) // 1024
if log_size > 1024:
    with open("log.txt", "w") as log_remover:
        log_remover.write("")
        log_remover.close()
        
# print('Size of file is', log_size, 'KB')
