# -*- coding:utf-8 -*-

import requests
import json
import unittest

class Chack(unittest.TestCase):
    def chack(self, url, payload, headers):
        try:
            r = requests.post(url, json=payload, headers=headers)
            self.result = r.json()

            self.assertEqual(self.result['code'], 0)
            self.assertEqual(self.result['msg'], u'查询成功')
            print(self.result)
        except (AttributeError, json.decoder.JSONDecodeError) as e:
            print(r.text)

        finally:
            if self.result['msg'] == '超过该张票当天查验次数' :
                print("失败原因：超过当天最大查验次数5次")
            elif self.result['code'] == 106:
                print("失败原因：监控到税局接口异常，可能会造成查验失败")
            elif self.result['code'] == 9999:
                print("失败原因：当前查验接口不稳定，可能会造成查验失败")






