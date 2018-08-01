"""
 Created by qujl on 2018-08-01
"""

# -*- coding:utf-8 -*-

__author__ = 'qujl'

import requests
import json
from interface import xml2json
from xml.etree import ElementTree as ET

url = "http://api.taxservices.cn/fpcyService/fpcyService.do"

payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION><FPLX>04</FPLX><FPDM>012001700211</FPDM><FPHM>06123066</FPHM><KPRQ>20180103</KPRQ><JYM>900465</JYM><USERNAME>banguser</USERNAME><SENDTIME>20180801145317</SENDTIME><SIGN>8d4bd98324d452ce6d0a9065cfd72d2e</SIGN></MSG>"
headers = {
    'Content-Type': "application/xml",
    'Cache-Control': "no-cache",
    'Postman-Token': "bbd87961-e4a1-4918-6c3f-f9a8e0907d36"
    }

response = requests.request("POST", url, data=payload, headers=headers)
info = response.text
result_str = (info.replace('<?xml version="1.0" encoding="UTF-8"?>', ''))


