# -*- coding:utf-8 -*-
# author：jinliang
# fileName: eck_interface_test.py
# used for:长软查验接口监控

import unittest
from interface.check import Check
from interface.jiami import *
from interface.datafile import *



class CheckInvoiceTest(unittest.TestCase):
    """各省发票查验接口监控报告"""



    def setUp(self):
        # 调用接口登录方法
        self.url = "http://check.fapiaoxx.com/invoice/check/"
        #self.url = "https://api.taxservices.cn/fpcyService/fpcyService.do"
        self.headers = {
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }

    # print(self.headers)

    def tearDown(self):
        pass

    def test_tianjin(self):
        """天津普通发票查验"""
        data = DataFile()
        payload = data.tianjin()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_shanghai(self):
        """上海普通发票查验"""
        data = DataFile()
        payload = data.shanghai()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_beijing(self):
        """北京普通发票查验"""
        data = DataFile()
        payload = data.beijing()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_hebei(self):
        """河北普通发票查验"""
        data = DataFile()
        payload = data.hebei()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_liaoning(self):
        """辽宁普通发票查验成功"""
        data = DataFile()
        payload = data.liaoning()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_anhui(self):
        """安徽普通发票查验"""
        data = DataFile()
        payload = data.anhui()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_henan(self):
        """河南普通发票查验"""
        data = DataFile()
        payload = data.henan()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_shenzhen(self):
        """深圳普通发票查验"""
        data = DataFile()
        payload = data.shenzhen()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_shanxi(self):
        """山西普通发票查验成功"""
        data = DataFile()
        payload = data.shanxi()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_neimeng(self):
        """内蒙普通发票查验"""
        data = DataFile()
        payload = data.neimeng()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_jilin(self):
        """吉林普通发票查验"""
        data = DataFile()
        payload = data.jilin()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_zhejiang(self):
        """浙江专用发票查验"""
        data = DataFile()
        payload = data.zhejiang()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_fujian(self):
        """福建普通发票查验"""
        data = DataFile()
        payload = data.fujian()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_jiangxi(self):
        """江西普通发票查验"""
        data = DataFile()
        payload = data.jiangxi()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_shandong(self):
        """山东普通发票查验"""
        data = DataFile()
        payload = data.shandong()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_hubei(self):
        """湖北普通发票查验"""
        data = DataFile()
        payload = data.hubei()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_hunan(self):
        """湖南普通发票查验"""
        data = DataFile()
        payload = data.hunan()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_guangdong(self):
        """广东普通发票查验"""
        data = DataFile()
        payload = data.guangdong()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_guangxi(self):
        """广西普通发票查验"""
        data = DataFile()
        payload = data.guangxi()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_hainan(self):
        """海南普通发票查验"""
        data = DataFile()
        payload = data.hainan()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_shaxi(self):
        """陕西普通发票查验"""
        data = DataFile()
        payload = data.shanxi()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)


    def test_yunnan(self):
        """云南普通发票查验`"""
        data = DataFile()
        payload = data.yunnan()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_heilongjiang(self):
        """黑龙江普通发票查验`"""
        data = DataFile()
        payload = data.heilongjiang()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)
    def test_guizhou(self):
        """贵州普通发票查验`"""
        data = DataFile()
        payload = data.guizhou()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_xizang(self):
        """西藏普通发票查验`"""
        data = DataFile()
        payload = data.xizang()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_gansu(self):
        """甘肃普通发票查验`"""
        data = DataFile()
        payload = data.gansu()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_qinghai(self):
        """青海普通发票查验`"""
        data = DataFile()
        payload = data.qinghai()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_ningxi(self):
        """宁夏普通发票查验`"""
        data = DataFile()
        payload = data.ningxi()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)

    def test_xinjiang(self):
        """新疆普通发票查验`"""
        data = DataFile()
        payload = data.xinjiang()
        test_check = Check()
        test_check.check(self.url, payload, self.headers)






    # def test_zyfp_success(self):
    #     """专用发票查验成功"""
    #     payload = {
    #         "fpdm": "1100171130",
    #         "fphm": "02577178",
    #         "fpje": "6320.75",
    #         "fplx": "01",
    #         "kprq": "20170816",
    #         "uniqueId": "1000004",
    #         "sign": "b132ef39f0e00d50b9986e8f7536ca30"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     self.result = r.json()
    #     if self.result['code'] == " ":
    #         print(r.text)
    #         self.assertEqual(self.result['code'], 0)
    #     else:
    #         # print(self.result)
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #
    # def test_fplx_null(self):
    #     """发票类型不能为空"""
    #     payload = {
    #         "fpdm": "014001700107",
    #         "fphm": "02560597",
    #
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10001)
    #             self.assertEqual(self.result['msg'], '发票类型：发票类型不能为空')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_fplx_error(self):
    #     """发票类型不合法"""
    #     payload = {
    #         "fpdm": "014001700107",
    #         "fphm": "02560597",
    #         "fplx": 10,
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10002)
    #             self.assertEqual(self.result['msg'], '发票类型：不合法的类型')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_fplx_existent(self):
    #     """发票类型不存在"""
    #     payload = {
    #         "fpdm": "014001700107",
    #         "fphm": "02560597",
    #         "fplx": "100",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10003)
    #             self.assertEqual(self.result['msg'], '发票类型：不存在的类型')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_fpdm_null(self):
    #     """发票代码不能为空"""
    #     payload = {
    #         "qpdm": "",
    #         "fphm": "02560597",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10004)
    #             self.assertEqual(self.result['msg'], '发票代码：发票代码不能为空')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_fpdm_error(self):
    #     """发票代码不合法"""
    #     payload = {
    #         "fpdm": 10,
    #         "fphm": "02560597",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10005)
    #             self.assertEqual(self.result['msg'], '发票代码：不合法的类型')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_fpdm_Overrun(self):
    #     """发票代码长度不合法"""
    #     payload = {
    #         "fpdm": "014001700107343",
    #         "fphm": "02560597",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10006)
    #             self.assertEqual(self.result['msg'], '发票代码：不合法的长度')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_fphm_null(self):
    #     """发票号码不能为空"""
    #     payload = {
    #         "fpdm": "014001700107",
    #         "qphm": "02560597",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10007)
    #             self.assertEqual(self.result['msg'], '发票号码：发票号码不能为空')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_fphm_error(self):
    #     """发票号码不合法"""
    #     payload = {
    #         "fpdm": "014001700107",
    #         "fphm": 342,
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10008)
    #             self.assertEqual(self.result['msg'], '发票号码：不合法的类型')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_fphm_Overrun(self):
    #     """发票号码长度不合法"""
    #     payload = {
    #         "fpdm": "014001700107",
    #         "fphm": "0256059712",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10009)
    #             self.assertEqual(self.result['msg'], '发票号码：不合法的长度')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_kprq_null(self):
    #     """开票日期不能为空"""
    #     payload = {
    #         "fpdm": "014001700107",
    #         "fphm": "02560597",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "qprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10010)
    #             self.assertEqual(self.result['msg'], '开票日期：开票日期不能为空')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_kprq_error(self):
    #     """开票日期不合法的类型"""
    #     payload = {
    #         "fpdm": "014001700107",
    #         "fphm": "02560597",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": 20170522,
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10011)
    #             self.assertEqual(self.result['msg'], '开票日期：不合法的类型')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_kprq_error2(self):
    #     """开票日期不合法的格式"""
    #     payload = {
    #         "fpdm": "1100171320",
    #         "fphm": "29688656",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "201705221",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10012)
    #             self.assertEqual(self.result['msg'], '开票日期：不合法的格式')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_fpje_null(self):
    #     """开票金额不能为空"""
    #     payload = {
    #         "fpdm": "014001700107",
    #         "fphm": "02560597",
    #         "kpje": "100.25",
    #         "fplx": "01",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10013)
    #             self.assertEqual(self.result['msg'], '开票金额：开票金额不能为空')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_fpje_error(self):
    #     """开票金额不合法的类型"""
    #     payload = {
    #         "fpdm": "014001700107",
    #         "fphm": "02560597",
    #         "fpje": 100.25,
    #         "fplx": "01",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10014)
    #             self.assertEqual(self.result['msg'], '开票金额：不合法的类型')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_kpje_error2(self):
    #     """开票金额不合法的格式"""
    #     payload = {
    #         "fpdm": "1100171320",
    #         "fphm": "29688656",
		# 	"fpje": "100",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10015)
    #             self.assertEqual(self.result['msg'], '开票金额：不合法的格式')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_jym_null(self):
    #     """校验码不能为空"""
    #     payload = {
    #         "fpdm": "1100171320",
    #         "fphm": "29688656",
    #         "fpje": "100.25",
    #         "fplx": "04",
    #         "sjym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10016)
    #             self.assertEqual(self.result['msg'], '检验码：检验码不能为空')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_jym_error(self):
    #     """校验码不合法的类型"""
    #     payload = {
    #         "fpdm": "1100171320",
    #         "fphm": "29688656",
    #         "fpje": "100.25",
    #         "fplx": "04",
    #         "jym": 1234,
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10017)
    #             self.assertEqual(self.result['msg'], '检验码：不合法的类型')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_jym_error2(self):
    #     """校验码长度不合法"""
    #     payload = {
    #         "fpdm": "1100171320",
    #         "fphm": "29688656",
    #         "fplx": "04",
    #         "jym": "86392634",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10018)
    #             self.assertEqual(self.result['msg'], '检验码：不合法的长度')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_only_null(self):
    #     """唯一标识：唯一标识不能为空"""
    #     payload = {
    #         "fpdm": "1100171320",
    #         "fphm": "29688656",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "quniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10019)
    #             self.assertEqual(self.result['msg'], '唯一标识：唯一标识不能为空')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_only_error(self):
    #     """唯一标识：不合法的唯一标识"""
    #     payload = {
    #         "fpdm": "1100171320",
    #         "fphm": "29688656",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "10000045",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10020)
    #             self.assertEqual(self.result['msg'], '唯一标识：不合法的唯一标识')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_sign_null(self):
    #     """签名：签名不能为空"""
    #     payload = {
    #         "fpdm": "1100171320",
    #         "fphm": "29688656",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "qsign": "054c7612b78f8c9bc37d6364103c3b0f"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10021)
    #             self.assertEqual(self.result['msg'], '签名：签名不能为空')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #
    # def test_sign_error(self):
    #     """签名：签名错误"""
    #     payload = {
    #         "fpdm": "1100171320",
    #         "fphm": "29688656",
    #         "fplx": "04",
    #         "jym": "863926",
    #         "kprq": "20170522",
    #         "uniqueId": "1000004",
    #         "sign": "054c7612b78f8c9bc37d6364103c3b0few"
    #     }
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] == " ":
    #             print(r.text)
    #             self.assertEqual(self.result['code'], 0)
    #         else:
    #             # print(self.result)
    #             self.assertEqual(self.result['code'], 10022)
    #             self.assertEqual(self.result['msg'], '签名：签名错误')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)