import os
import sys
import urllib
from time import sleep

url = "http://cpaexam.cicpa.org.cn"


def getcode(url):
    return urllib.urlopen(url).getcode()


while sys.platform == 'darwin':
    try:
        status = getcode(url)
        if status in [200, 301]:
            for i in range(10):
                os.system('say "Site is online."')
                sleep(0.5)
    except:
        print('Site is offline, wait 5 seconds to retry.')
        sleep(5)
        pass
else:
    print('This script only supports OS X.')
