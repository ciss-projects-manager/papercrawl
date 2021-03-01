import requests
from lxml import etree
from sotapage import sotaPage

class areaPage(object):
    def __init__(self):
        self.baseurl = 'https://www.paperswithcode.com/'
        self.taskdict = sotaPage.request_sotapage()

    def request_area(self):
        pass


