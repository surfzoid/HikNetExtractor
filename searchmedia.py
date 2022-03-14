#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from hashlib import new


def GetVideoList(XmlData):
    open("searchresult.xml", 'w').write(XmlData)
    xmlroot = ET.fromstring(XmlData)

    # Uses a list comprehension and element tree's iterparse function to create a dictionary containing the namespace prefix and it's uri. The underscore is utilized to remove the "start-ns" output from the list.
    #namespaces = {node[0]: node[1] for _, node in ET.iterparse("searchresult.xml", events=['start-ns'])}
    namespaces = {node[0]: node[1] for _, node in ET.iterparse(
        "searchresult.xml", events=['start-ns'])}
    # Iterates through the newly created namespace list registering each one.
    for key, value in namespaces.items():
        ET.register_namespace(key, value)
    # The curly brackets are needed around the uri when using Element Tree's find command with a manually passed namespace.
    default_ns = "{" + namespaces[""] + "}"

    # By inserting your namespace variable immediately before the search term your code will return the results you expect.
    #activ_tag = xmlroot.find(".//" + default_ns + "playbackURI")
    rtspuri = xmlroot.findall(".//" + default_ns + "playbackURI")
    rtspurilist = []
    for rtspurielement in rtspuri:
        rtspurilist.append(rtspurielement.text)
        # print(rtspurielement.text)
    return rtspurilist
