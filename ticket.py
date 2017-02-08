#!/usr/bin/python

import urllib2
import urllib
import time
import sys
import socket
import json, time

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

def getTicket(date):
    seatList = ['ze_num', 'rw_num', 'yw_num', 'yz_num']

    code, line = post('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=' + date + \
            '&leftTicketDTO.from_station=CZQ&leftTicketDTO.to_station=BJP&purpose_codes=ADULT', None)

    if code == 200:
        ticketList = json.loads(line)['data']
        results = []

        for t in ticketList:
            t = t['queryLeftNewDTO']

            res = []
            res.append(t['station_train_code'])
            for s in seatList:
                res.append(t[s])

            results.append(res)
        
        print('%5s %5s %5s %5s %5s' % ('', 'ED', 'RW', 'YW', 'YZ'))
        for res in results:
            for i, s in enumerate(res):
                if s == '--' or s == u'\u65e0':
                    res[i] = ''
                
            print('%5s %5s %5s %5s %5s' % (res[0], res[1], res[2], res[3], res[4]))

def ticket():
    date = time.strftime("%Y-%m-%d")
    endDate = '2017-02-07'

    while date < endDate:
        print(date)
        getTicket(date)
        datePre = date[:-1]
        dateLast = date[-1:]
        date = datePre + str(int(dateLast)+1)


if __name__ == '__main__':
    ticket()

    
