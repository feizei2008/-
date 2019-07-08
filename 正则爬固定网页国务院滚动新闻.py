# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:47:39 2017

@author: zack zhang
"""
#import tushare as ts
#from threading import Timer
#
#def sinanews(): 
#  print ts.get_latest_news(top=9) 
#  t = Timer(10, sinanews) 
#  t.start() 
#    
#if __name__ == "__main__": 
#  sinanews()      
  
#http://blog.csdn.net/whiterbear/article/details/50232637

#from bs4 import BeautifulSoup
import urllib2
import re
from threading import Timer
import logging
import os
import ctypes
from retrying import retry

os.path.dirname(os.path.abspath("正则爬固定网页国务院滚动新闻.py"))

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED = 0x04 # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN

STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

class Logger:
    def __init__(self, path,clevel = logging.DEBUG,Flevel = logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        #设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        #设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)
 
    def debug(self,message):
        self.logger.debug(message)
 
    def info(self,message):
        self.logger.info(message)
 
    def war(self,message,color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warn(message)
        set_color(FOREGROUND_WHITE)
 
    def error(self,message,color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(message)
        set_color(FOREGROUND_WHITE)
 
    def cri(self,message):
        self.logger.critical(message)
        
#def dd():
#    def chufa(x,y):
#        print x/y        
#    try:
#        chufa(2,0)
#    except Exception, e:
#        Logger('e.log').error(e)
#    Timer(20,dd).start()     
#if __name__ == "__main__": 
#    dd()
       
#if __name__ =='__main__':
#    logyyx = Logger('yyx.log',logging.ERROR,logging.DEBUG)
#    logyyx.debug('一个debug信息')
#    logyyx.info('一个info信息')
#    logyyx.war('一个warning信息')
#    logyyx.error('一个error信息')
#    logyyx.cri('一个致命critical信息')
   
url = 'http://www.gov.cn/xinwen/gundong.htm'
#response = urllib2.urlopen(url).read().decode('utf8',errors='replace')

def getHtml(url):
    m = urllib2.urlopen(url)
    html = m.read()
    return html
#    try:
#	    m = urllib2.urlopen(url)
#	    html = m.read()
#	    return html
##    except urllib2.HTTPError, e:
##        print e.code
##        print e.reason
#    except urllib2.URLError, e:
#        if hasattr(e,"code"):
#            print e.code
#        if hasattr(e,"reason"):
#            print e.reason
#    else:
#        print "Retrying pls wait..."

def getData(html):
    pattern = r'<a href=.*?>(.*?)</a>'
    p = re.compile(pattern)
    data = re.findall(p,html)
    return data
#    try:
#        pattern = r'<a href=.*?>(.*?)</a>'
#        p = re.compile(pattern)
#        data = re.findall(p,html)
#        return data
#    except TypeError, e:
#        print e
#        #logging.exception(e)
#    finally:
#        print "finally..."
#def wait(x):
#    print "Retrying in %d seconds" % (x)
    
@retry(stop_max_attempt_number=15, wait_exponential_multiplier=5000, wait_exponential_max=40000) 
def GOVGunDong():
    for i in getData(getHtml(url))[1:8]:
        try:
            print i.decode('utf-8')
        except Exception, e:
            loggwy = Logger(u"正则爬固定网页国务院滚动新闻.log")
#            loggwy.debug(e)
#            loggwy.info(e)
#            loggwy.war(e)
            loggwy.error(e)
#            loggwy.cri(e)
#            print e+"Retrying in 30 seconds"
#    Timer(20,wait(20)).start()    
    print "#"*60        
    t = Timer(30,GOVGunDong)
    t.start()
#    for i in getData(getHtml(url))[1:8]:
#        print i.decode('utf-8')
#    print "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+="
#    t = Timer(30,GOVGunDong)
#    t.start()
   
if __name__ == "__main__": 
    GOVGunDong()
  
#  loggwy = Logger(u"正则爬固定网页国务院滚动新闻.log",logging.ERROR,logging.DEBUG)
#  loggwy.debug('一个debug信息')
#  loggwy.info('一个info信息')
#  loggwy.war('一个warning信息')
#  loggwy.error('一个error信息')
#  loggwy.cri('一个致命critical信息')