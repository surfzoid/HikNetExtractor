#!/usr/bin/env python3

url = '192.168.xx.xx:80'
username = 'admin'
password = 'the password'
# 101 first stream, 102 second stream, etc
Channel = '101'
# end with "/"
SavePath = "/tmp/hikextracted/camptz2/"
# perhaps in the future, from now, use one HikNetExtract instance by cam
CamName = ""
DaysToKeep = 30
# if "yes", UTC time offset of the computer is aply to end and start time of the file name.
UtcTOfset = "yes"
