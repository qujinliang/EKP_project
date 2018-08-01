# -*- coding:utf-8 -*-
# author：jinliang
# fileName: check.py
# used for:长软查验发票

import requests
import json
import unittest


class Check(unittest.TestCase):
    BL = bool
    '''
        这是一个查验模块，Check是查验类，集成了unittest.TestCase类
        它有一个check方法，需要传三个参数，url,payload,headers
        url:要请求的接口地址
        payload:请求的参数集合
        headers：请求的头部信息
        直接对请求的结果进行断言，并打印结果
    '''
    def check(self, url, payload, headers):
        try:
            self.r = requests.request("POST",url, data=payload, headers=headers)
            self.result = self.r.text
            if "<CYJGDM>001</CYJGDM>" in self.result:
                CODE = 0
            elif "<CYJGDM>106</CYJGDM>" in self.result:
                CODE = 106
            elif "<CYJGDM>001</CYJGDM>" in self.result:
                CODE = 9999
            else:
                CODE = 88888
            self.assertEqual(CODE, 0)
            # self.assertEqual(self.result['msg'], u'请求成功')
            print(self.result)
        except (AttributeError, json.decoder.JSONDecodeError) as e:
            print(e)

        finally:
            if self.r.text:
                if CODE == 106:
                    print("失败原因：监控到税局接口异常，可能会造成查验失败")
                    Check.BL = False
                elif CODE == 9999:
                    print("失败原因：当前查验接口不稳定，可能会造成查验失败")
                    Check.BL = False
                elif CODE != 0:
                    print(self.r.text)
                    Check.BL = False

            else:
                print("失败原因：请求查验接口超时！")
                Check.BL = False
                self.assertEqual(504,0)











