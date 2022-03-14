#!/usr/bin/env python3

import json
from datetime import datetime

import requests
from requests.auth import HTTPDigestAuth

from config import password, url, username

#filename = str(datetime.now().strftime("%m-%d-%Y_%H:%M:%S")) + "nofilename.mp4"


def ActionGetSimple(Wanted):
    r = requests.get(url="http://" + url + Wanted, allow_redirects=True,
                     auth=HTTPDigestAuth(username, password), timeout=15)
    print(r.text)


def ActionGetSimplejson(Wanted):
    r = json.load(requests.get(url="http://" + url + Wanted, allow_redirects=True,
                               auth=HTTPDigestAuth(username, password), timeout=15).json())
    print(r.title())


def ActionPost(Wanted, XmlData):
    r = requests.post(url="http://" + url + Wanted, auth=HTTPDigestAuth(username,
                                                                        password), data=XmlData, stream=True, timeout=15)
    # print(r.text)
    return r.text


def ActionPostSimple(Wanted):
    r = requests.post(url="http://" + url + Wanted, auth=HTTPDigestAuth(username,
                                                                        password), stream=True, timeout=15)
    print(r.text)


def ActionGet(Wanted, XmlData):
    r = requests.get(url="http://" + url + Wanted, auth=HTTPDigestAuth(username,
                                                                       password), data=XmlData, stream=True, timeout=15)
    print(r.text)


def ActionPut(Wanted):
    r = requests.put("http://" + url + Wanted,
                     auth=HTTPDigestAuth(username, password), timeout=15)
    print(r.text)


def ActionPut(Wanted):
    r = requests.put("http://" + url + Wanted,
                     auth=HTTPDigestAuth(username, password), timeout=15)
    print(r.text)


def ActionDllFile(Wanted, filename, XmlData):
    try:
        r = requests.post(url="http://" + url + Wanted, stream=True,
                          allow_redirects=True, auth=HTTPDigestAuth(username, password), timeout=15)
        if "badXmlContent" in str(r.content):
            r = requests.get(url="http://" + url + "/ISAPI/ContentMgmt/download", data=XmlData,
                             stream=True, allow_redirects=True, auth=HTTPDigestAuth(username, password), timeout=15)
            # print(r.content)
        open(filename, 'wb').write(r.content)
    except requests.exceptions.Timeout as t:
        # Maybe set up for a retry, or continue in a retry loop
        print(t)
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print("Too Many Redirects")
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(e)
        raise SystemExit(e)
