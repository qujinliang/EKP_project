# -*- coding:utf-8 -*-


import unittest
from interface.chack import Chack
from interface.jiami import *



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
        payload = {
            "fpdm": "1200172320",
            "fphm": "09064299",
            "fplx": "04",
            "jym": "212144",
            "kprq": "20171023",
            "uniqueId": "1000004",
            "sign": md5("fpdm=1200172320&fphm=09064299&fplx=04&jym=212144&kprq=20171023&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }

        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)



    def test_shanghai(self):
        """上海普通发票查验"""
        payload = {
            "fpdm": "3100171320",
            "fphm": "48702542",
            "fplx": "04",
            "jym": "822595",
            "kprq": "20170612",
            "uniqueId": "1000004",
            "sign": md5("fpdm=3100171320&fphm=48702542&fplx=04&jym=822595&kprq=20170612&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)


    def test_beijing(self):
        """北京普通发票查验"""
        payload = {
            "fpdm": "1100171320",
            "fphm": "29688656",
            "fplx": "04",
            "jym": "079367",
            "kprq": "20170514",
            "uniqueId": "1000004",
            "sign":md5("fpdm=1100171320&fphm=29688656&fplx=04&jym=079367&kprq=20170514&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_hebei(self):
        """河北普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '1300171320', 'fphm': '00271772', 'jym': '936815',
                   'kprq': '20170927','uniqueId':'1000004',
                   'sign':md5("fpdm=1300171320&fphm=00271772&fplx=04&jym=936815&kprq=20170927&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_liaoning(self):
        """辽宁普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '2100171320', 'fphm': '11695353', 'jym': '893273',
                   'kprq': '20170925','uniqueId':'1000004',
                   'sign':md5("fpdm=2100171320&fphm=11695353&fplx=04&jym=893273&kprq=20170925&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_anhui(self):
        """安徽普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '3400172320', 'fphm': '19768327','jym': '156228',
                   'kprq': '20171020','uniqueId':'1000004',
                   'sign':md5("fpdm=3400172320&fphm=19768327&fplx=04&jym=156228&kprq=20171020&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_henan(self):
        """河南普通发票查验"""
        payload = {'fplx': '01', 'fpdm': '4100162130', 'fphm': '16971475', 'fpje': '7250.25',
                   'kprq': '20170809','uniqueId':'1000004',
                   'sign':md5("fpdm=4100162130&fphm=16971475&fpje=7250.25&fplx=01&kprq=20170809&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def testshenzhen(self):
        """深圳普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '4403162320', 'fphm': '66718525',  'jym': '520590',
                   'kprq': '20170814','uniqueId':'1000004',
                   'sign':md5("fpdm=4403162320&fphm=66718525&fplx=04&jym=520590&kprq=20170814&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)



    def test_check_invoice_shanxi(self):
        """山西普通发票查验成功"""
        payload = {'fplx': '01', 'fpdm': '1400171130', 'fphm': '02062714', 'fpje': '17094.03',
                   'kprq': '20171117','uniqueId':'1000004',
                   'sign':md5("fpdm=1400171130&fphm=02062714&fpje=17094.03&fplx=01&kprq=20171117&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}



    def test_neimeng(self):
        """内蒙普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '1500164350', 'fphm': '01058176', 'jym': '119257',
                   'kprq': '20170720','uniqueId':'1000004',
                   'sign':md5("fpdm=1500164350&fphm=01058176&fplx=04&jym=119257&kprq=20170720&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)



    def test_jilin(self):
        """吉林普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '2200162350', 'fphm': '01875257', 'jym': '878078',
                   'kprq': '20171115','uniqueId':'1000004',
                   'sign':md5("fpdm=2200162350&fphm=01875257&fplx=04&jym=878078&kprq=20171115&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_zhejiang(self):
        """浙江专用发票查验"""
        payload = {'fplx': '01', 'fpdm': '3300154130', 'fphm': '05331852',  'fpje': '53.68',
                   'kprq': '20171010','uniqueId':'1000004',
                   'sign':md5("fpdm=3300154130&fphm=05331852&fpje=53.68&fplx=01&kprq=20171010&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_fujian(self):
        """福建普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '3500163350', 'fphm': '21099644', 'jym': '920870',
                   'kprq': '20170621','uniqueId':'1000004',
                   'sign':md5("fpdm=3500163350&fphm=21099644&fplx=04&jym=920870&kprq=20170621&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_jiangxi(self):
        """江西普通发票查验"""
        payload = {'fplx': '01', 'fpdm': '3600163130', 'fphm': '06998169', 'fpje': '1522.64',
                   'kprq': '20171018','uniqueId':'1000004',
                   'sign':md5("fpdm=3600163130&fphm=06998169&fpje=1522.64&fplx=01&kprq=20171018&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_shandong(self):
        """山东普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '3700164320', 'fphm': '33170062', 'jym': '690447',
                   'kprq': '20170606','uniqueId':'1000004',
                   'sign':md5("fpdm=3700164320&fphm=33170062&fplx=04&jym=690447&kprq=20170606&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_hubei(self):
        """湖北普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '4200164320', 'fphm': '47982351', 'jym': '464625',
                   'kprq': '20171026','uniqueId':'1000004',
                   'sign':md5("fpdm=4200164320&fphm=47982351&fplx=04&jym=464625&kprq=20171026&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_hunan(self):
        """湖南普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '4300171320', 'fphm': '04268504', 'jym': '288558',
                   'kprq': '20170616','uniqueId':'1000004',
                   'sign':md5("fpdm=4300171320&fphm=04268504&fplx=04&jym=288558&kprq=20170616&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_guangdong(self):
        """广东普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '4400163320', 'fphm': '36198951', 'jym': '596043',
                   'kprq': '20170421','uniqueId':'1000004',
                   'sign':md5("fpdm=4400163320&fphm=36198951&fplx=04&jym=596043&kprq=20170421&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_guangxi(self):
        """广西普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '4500171320', 'fphm': '15663941', 'jym': '249570',
                   'kprq': '20170612','uniqueId':'1000004',
                   'sign':md5("fpdm=4500171320&fphm=15663941&fplx=04&jym=249570&kprq=20170612&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_hainan(self):
        """海南普通发票查验"""
        payload = {'fplx': '01', 'fpdm': '4600163130', 'fphm': '01208520',
                   'fpje': '816610.26','kprq': '20171123','uniqueId':'1000004',
                   'sign':md5("fpdm=4600163130&fphm=01208520&fpje=816610.26&fplx=01&kprq=20171123&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_shaxi(self):
        """陕西普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '6100171320', 'fphm': '09030275',  'jym': '911427',
                   'kprq': '20170626','uniqueId':'1000004',
                   'sign':md5("fpdm=6100171320&fphm=09030275&fplx=04&jym=911427&kprq=20170626&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)


    def test_yunnan(self):
        """云南普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '5300171320', 'fphm': '13826269', 'jym': '578163',
                    'kprq': '20171119', 'uniqueId': '1000004',
                    'sign': md5("fpdm=5300171320&fphm=13826269&fplx=04&jym=578163&kprq=20171119&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_heilongjiang(self):
        """黑龙江普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '2300173320', 'fphm': '12299469', 'jym': '239171',
                    'kprq': '20180203', 'uniqueId': '1000004',
                    'sign': md5("fpdm=2300173320&fphm=12299469&fplx=04&jym=239171&kprq=20180203&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_guizhou(self):
        """贵州普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '5200173320', 'fphm': '07708742', 'jym': '407547',
                    'kprq': '20180127', 'uniqueId': '1000004',
                    'sign': md5("fpdm=5200173320&fphm=07708742&fplx=04&jym=407547&kprq=20180127&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_xizang(self):
        """西藏普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '5400171320', 'fphm': '01316456', 'jym': '536623',
                    'kprq': '20171209', 'uniqueId': '1000004',
                    'sign': md5("fpdm=5400171320&fphm=01316456&fplx=04&jym=536623&kprq=20171209&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_gansu(self):
        """甘肃普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6200171350', 'fphm': '00324121', 'jym': '376901',
                    'kprq': '20180227', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6200171350&fphm=00324121&fplx=04&jym=376901&kprq=20180227&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_qinghai(self):
        """青海普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6300162350', 'fphm': '02226976', 'jym': '163565',
                    'kprq': '20180113', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6300162350&fphm=02226976&fplx=04&jym=163565&kprq=20180113&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_ningxi(self):
        """宁夏普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6400173320', 'fphm': '02748815', 'jym': '197261',
                    'kprq': '20180323', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6400173320&fphm=02748815&fplx=04&jym=197261&kprq=20180323&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)

    def test_xinjiang(self):
        """新疆普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6500174320', 'fphm': '04312540', 'jym': '393788',
                    'kprq': '20180111', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6500174320&fphm=04312540&fplx=04&jym=393788&kprq=20180111&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        test_chack = Chack()
        test_chack.chack(self.url, payload, self.headers)






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