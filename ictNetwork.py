#!/usr/bin/python

import urllib2
import urllib
import time
import sys
import socket  

def post(url, data):
    success = False
    while not success:
        try:
            req = urllib2.Request(url)
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
            response = opener.open(req, data, timeout=3)
            code = response.code
            line = response.next()
            success = True
        except:
            time.sleep(5)
    return code, line


def ictNetworkLogin():
    url = 'http://159.226.39.22/cgi-bin/do_login'
    data = {'username':'chengang2016',
        'password':'5bb074ecd14055ad',
            'drop':'0',
            'type':'1',
            'n':'100'}
    data = urllib.urlencode(data)
    return post(url, data)

if __name__ == '__main__':
    socket.setdefaulttimeout(10.0)   

    while True:
        code, line = post('http://www.w3school.com.cn/h.asp', None)
        if str.find(line, '159') != -1:
            print "W3S %s %s"%(time.strftime("%m-%d %H-%M-%S", 
                        time.localtime()), 'Failed')

            code, line = ictNetworkLogin()
            print "ICT %s %d"%(time.strftime("%m-%d %H-%M-%S", 
                        time.localtime()), code)
        else:
            print "W3S %s %s"%(time.strftime("%m-%d %H-%M-%S", 
                        time.localtime()), 'OK')

        sys.stdout.flush()
        time.sleep(10)

