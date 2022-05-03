#!/usr/bin/env python3
# ===============================================================================
# @package HikNetExtractor
#
# Provides functionality to extract perodicly record event from
# Hikvion camera or NVR with ISAPI and HTTPDigestAuth enable.
# Add this script to an shedle task and you will keep records
# durring the number of day you put in the config.
#
# See also: http://www.hikvision.com/en/download.asp
#
# ===============================================================================

from datetime import datetime
import sys
from time import strftime

from prompt_toolkit import Application
import psutil

from Actions import ActionPost
from filesManager import donloadfs
from searchmedia import GetVideoList
from xmlreq import __SEARCH_MEDIA_XML

gettrace= sys.gettrace()

# For debugging
debug_status=True if gettrace else False
if debug_status:
    print("\033[1;31;40m Running in debug IDE")
else:
    print("\033[1;32;40m Running outside debug IDE")
    procs = [p for p in psutil.process_iter() if 'python' in p.name() and __file__ in p.cmdline()]
    if len(procs) > 1:
        print('Process is already running...')
        sys.exit(1)
 


    
print(str(datetime.now()))
print(strftime('%z'))
# DelOldestDir()
# Action('/ISAPI/System/reboot')
# ActionGetSimple('/ISAPI/ContentMgmt/record/tracks')
# ActionGetSimple('/ISAPI/System/Time')
# ActionGetSimple('/ISAPI/ContentMgmt/search/profile')
#ActionGet('/ISAPI/ContentMgmt/download' , __DOWNLOAD_REQUEST_XML)
#ActionPost('/ISAPI/ContentMgmt/record/tracks/10" + Channel + "1/dailyDistribution', __XML_trackDailyParam)
#Answer = ActionPost('/ISAPI/ContentMgmt/search',__SEARCH_MEDIA_XML)
Answer = ActionPost('/ISAPI/ContentMgmt/search', __SEARCH_MEDIA_XML)
donloadfs(GetVideoList(Answer))

# ActionPut('/ISAPI/Security/sessionHeartbeat')
# ActionGetSimplejson('/ISAPI/Security/token?format=json')
# ActionDllFile('/ISAPI/ContentMgmt/download?playbackURI=rtsp://192.168.27.67/Streaming/tracks/10" + Channel + "1?starttime=2022-03-11%2003:00:52Z&amp;endtime=2022-03-11%2003:06:05Z&amp;name=08000000014000413&amp;size=25236932')
