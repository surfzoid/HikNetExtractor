#!/usr/bin/env python3

from asyncio.log import logger
import json
from datetime import datetime
import os
import sys
import time
from urllib.parse import urlparse

import requests
from requests.auth import HTTPDigestAuth

from config import password, url, username
from colored import *

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
        with requests.post(url="http://" + url + Wanted, stream=True,
                          allow_redirects=True, auth=HTTPDigestAuth(username, password), timeout=15) as r:
            if not "200" in str(r.status_code):
                r = requests.get(url="http://" + url + "/ISAPI/ContentMgmt/download", data=XmlData, stream=True, allow_redirects=True, auth=HTTPDigestAuth(username, password), timeout=15)
    
            total_length = r.headers.get('content-length')
            dl = 0
            total_length = int(total_length)
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=2097152): 
                    if chunk: # filter out keep-alive new chunks
                        
                        dl += len(chunk)
                        done = int(50 * dl / total_length)
                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                        sys.stdout.flush()
            
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
            r.close           
        #open(filename, 'wb').write(r.content)
    except requests.exceptions.Timeout as t:
        # Maybe set up for a retry, or continue in a retry loop
        print(t)
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print(CRED + "Too Many Redirects" + CEND)
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(e)
        #raise SystemExit(e)


def download(url: str, file_path='', attempts=2):
    """Downloads a URL content into a file (with large file support by streaming)

    :param url: URL to download
    :param file_path: Local file name to contain the data downloaded
    :param attempts: Number of attempts
    :return: New file path. Empty string if the download failed
    """
    if not file_path:
        file_path = os.path.realpath(os.path.basename(url))
    logger.info(f'Downloading {url} content to {file_path}')
    url_sections = urlparse(url)
    if not url_sections.scheme:
        logger.debug('The given url is missing a scheme. Adding http scheme')
        url = f'http://{url}'
        logger.debug(f'New url: {url}')
    for attempt in range(1, attempts+1):
        try:
            if attempt > 1:
                time.sleep(10)  # 10 seconds wait time between downloads
            with requests.post(url, stream=True,
                          allow_redirects=True, auth=HTTPDigestAuth(username, password), timeout=15) as response:
                response.raise_for_status()
                with open(file_path, 'wb') as out_file:
                    for chunk in response.iter_content(chunk_size=1024*1024):  # 1MB chunks
                        out_file.write(chunk)
                logger.info('Download finished successfully')
                return file_path
        except Exception as ex:
            logger.error(f'Attempt #{attempt} failed with error: {ex}')
    return ''
