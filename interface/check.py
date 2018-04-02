# -*- coding:utf-8 -*-
# author：jinliang
# fileName: check.py
# used for:长软查验发票

import requests
import json
import unittest

'''
    这是一个查验模块，Check是查验类，集成了unittest.TestCase类
    它有一个check方法，需要传三个参数，url,payload,headers
    url:要请求的接口地址
    payload:请求的参数集合
    headers：请求的头部信息
    直接对请求的结果进行断言，并打印结果
'''
class Check(unittest.TestCase):
    def check(self, url, payload, headers):
        try:
            self.r = requests.post(url, json=payload, headers=headers)
            self.result = self.r.json()

            self.assertEqual(self.result['code'], 0)
            self.assertEqual(self.result['msg'], u'查询成功')
            print(self.result)
        except (AttributeError, json.decoder.JSONDecodeError) as e:
            print(e)

        finally:
            if self.r:
                if self.result['code'] == 106:
                    print("失败原因：监控到税局接口异常，可能会造成查验失败")
                elif self.result['code'] == 9999:
                    print("失败原因：当前查验接口不稳定，可能会造成查验失败")
                elif self.result['code'] != 0:
                    print(self.r.text)
            else:
                print("失败原因：请求查验接口超时！")
                self.assertEqual(504,0)










