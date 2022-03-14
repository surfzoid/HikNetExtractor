#!/usr/bin/env python3

from datetime import datetime

from config import Channel, password, username

ToDay = datetime.now().strftime("%Y-%m-%d")
startTime = ToDay + "T00:00:00Z"
endTime = ToDay + "T23:59:59Z"

__SEARCH_MEDIA_XML = "<?xml version=\"1.0\" encoding=\"utf-8\"?><CMSearchDescription><searchID>D96991DE-5108-48FC-8767-8A786CB3E03E</searchID><trackList><trackID>" + Channel + "</trackID></trackList><timeSpanList><timeSpan><startTime>" + startTime + "</startTime><endTime>" + \
    endTime + "</endTime></timeSpan></timeSpanList><maxResults>50</maxResults><searchResultPostion>0</searchResultPostion><metadataList><metadataDescriptor>//recordType.meta.std-cgi.com</metadataDescriptor></metadataList></CMSearchDescription>"

__exDOWNLOAD_REQUEST_XML = "<?xml version='1.0'?><downloadRequest><playbackURI>rtsp://192.168.8.147/Streaming/tracks/1" + Channel + \
    "01/?starttime=20220306T111822Z&amp;endtime=20220306T112352Z&amp;name=ch01_08000000000000813&amp;size=78266368</playbackURI></downloadRequest>"


def DllXmlReq(rtspuri):
    rtspuri = rtspuri.replace("&", "&amp;")
    __DOWNLOAD_REQUEST_XML = "<?xml version=\"1.0\" encoding=\"utf-8\"?><downloadRequest version=\"1.0\" xmlns=\"http://www.isapi.org/ver20/XMLSchema\"><playbackURI>" + \
        rtspuri + "</playbackURI><userName>" + username + \
        "</userName><password>" + password + "</password></downloadRequest>"
    return __DOWNLOAD_REQUEST_XML


__XML_trackDailyParam = "<?xml version=\"1.0\" encoding=\"utf-8\"?><trackDailyParam><year>2022</year><monthOfYear>3</monthOfYear></trackDailyParam>"

__XML_downloadRequest = """\
<downloadRequest version="1.0" xmlns="http://www.isapi.org/ver20/XMLSchema">
<playbackURI>
<!--req, xs:string, playback URL, returned by the search service. It contains the information of file name and size,
e.g., <playbackURI>rtsp://192.168.27.67/Streaming/tracks/101?starttime=2022-03-11%2003:00:52Z&endtime=2022-03-11%2003:06:05Z&name=08000000014000413&size=25236932</playbackURI>-->
</playbackURI>
<userName><!--opt, xs:string,double verification user name--></userName>
<password><!--opt, xs:string,double verification password--></password>
</downloadRequest>"""

__XML_trackDailyDistribution = """\
    <trackDailyDistribution version="1.0" xmlns="http://www.isapi.com/ver20/XMLSchema">
<dayList>
<day>
<id><!--req, xs: integer, ID--></id>
<dayOfMonth><!--req, xs: integer, day of the month, starts from 1st--></dayOfMonth>
<record><!--req, xs: boolean, true-with video, false-no video--></record>
<recordType>
<!--req, xs: string, record type: time-continuous recording; event-record based on event-->
</recordType>
</day>
</dayList>
</trackDailyDistribution>"""
