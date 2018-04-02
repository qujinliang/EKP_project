from interface.jiami import *

'''发票数据存储模块'''

class DataFile():

    def tianjin(self):
        """天津普通发票查验"""
        payload = {
            "fpdm": "1200172320","fphm": "09064299","fplx": "04","jym": "212144","kprq": "20171023","uniqueId": "1000004",
            "sign": md5("fpdm=1200172320&fphm=09064299&fplx=04&jym=212144&kprq=20171023""&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }
        return payload

    def shanghai(self):
        """上海普通发票查验"""
        payload = {
            "fpdm": "3100172320","fphm": "87120411","fplx": "04","jym": "468403","kprq": "20180103","uniqueId": "1000004",
            "sign": md5("fpdm=3100172320&fphm=87120411&fplx=04&jym=468403&kprq=20180103&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }
        return payload

    def beijing(self):
        """北京普通发票查验"""
        payload = {
            "fpdm": "1100173320","fphm": "58929139","fplx": "04","jym": "056970","kprq": "20180103","uniqueId": "1000004",
            "sign":md5("fpdm=1100173320&fphm=58929139&fplx=04&jym=056970&kprq=20180103&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }
        return payload

    def hebei(self):
        """河北普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '1300171320', 'fphm': '00271772', 'jym': '936815', 'kprq': '20170927','uniqueId': '1000004',
            'sign': md5("fpdm=1300171320&fphm=00271772&fplx=04&jym=936815&kprq=20170927&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def liaoning(self):
        """辽宁普通发票查验成功"""
        payload = {
            'fplx': '04', 'fpdm': '2100171320', 'fphm': '11695353', 'jym': '893273', 'kprq': '20170925','uniqueId': '1000004',
            'sign': md5("fpdm=2100171320&fphm=11695353&fplx=04&jym=893273&kprq=20170925&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def anhui(self):
        """安徽普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '3400172320', 'fphm': '19768327','jym': '156228','kprq': '20171020','uniqueId':'1000004',
                   'sign':md5("fpdm=3400172320&fphm=19768327&fplx=04&jym=156228&kprq=20171020&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def henan(self):
        """河南普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '4100173320', 'fphm': '06001047', 'jym': '489592','kprq': '20180105', 'uniqueId': '1000004',
            'sign': md5("fpdm=4100173320&fphm=06001047&fplx=04&jym=489592&kprq=20180105&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def shenzhen(self):
        """深圳普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '4403162320', 'fphm': '66718525',  'jym': '520590','kprq': '20170814','uniqueId':'1000004',
                   'sign':md5("fpdm=4403162320&fphm=66718525&fplx=04&jym=520590&kprq=20170814&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def shanxi(self):
        """山西普通发票查验成功"""
        payload = {
            'fplx': '01', 'fpdm': '1400171130', 'fphm': '02062714', 'fpje': '17094.03','kprq': '20171117','uniqueId':'1000004',
            'sign':md5("fpdm=1400171130&fphm=02062714&fpje=17094.03&fplx=01&kprq=20171117&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def neimeng(self):
        """内蒙普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '1500171320', 'fphm': '11610387', 'jym': '496101','kprq': '20180113','uniqueId':'1000004',
            'sign':md5("fpdm=1500171320&fphm=11610387&fplx=04&jym=496101&kprq=20180113&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def jilin(self):
        """吉林普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '2200162350', 'fphm': '01875257', 'jym': '878078','kprq': '20171115','uniqueId':'1000004',
            'sign':md5("fpdm=2200162350&fphm=01875257&fplx=04&jym=878078&kprq=20171115&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def zhejiang(self):
        """浙江专用发票查验"""
        payload = {
            'fplx': '01', 'fpdm': '3300154130', 'fphm': '05331852',  'fpje': '53.68','kprq': '20171010','uniqueId':'1000004',
            'sign':md5("fpdm=3300154130&fphm=05331852&fpje=53.68&fplx=01&kprq=20171010&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def fujian(self):
        """福建普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '3500163320', 'fphm': '50657158', 'jym': '912642','kprq': '20180102','uniqueId':'1000004',
            'sign':md5("fpdm=3500163320&fphm=50657158&fplx=04&jym=912642&kprq=20180102&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def jiangxi(self):
        """江西普通发票查验"""
        payload = {
            'fplx': '01', 'fpdm': '3600163130', 'fphm': '06998169', 'fpje': '1522.64','kprq': '20171018','uniqueId':'1000004',
            'sign':md5("fpdm=3600163130&fphm=06998169&fpje=1522.64&fplx=01&kprq=20171018&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def shandong(self):
        """山东普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '3700171320', 'fphm': '22052218', 'jym': '728827','kprq': '20180105','uniqueId':'1000004',
            'sign':md5("fpdm=3700171320&fphm=22052218&fplx=04&jym=728827&kprq=20180105&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def hubei(self):
        """湖北普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '4200164320', 'fphm': '47982351', 'jym': '464625','kprq': '20171026','uniqueId':'1000004',
            'sign':md5("fpdm=4200164320&fphm=47982351&fplx=04&jym=464625&kprq=20171026&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def hunan(self):
        """湖南普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '4300173320', 'fphm': '02188236', 'jym': '883431','kprq': '20180103','uniqueId':'1000004',
            'sign':md5("fpdm=4300173320&fphm=02188236&fplx=04&jym=883431&kprq=20180103&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def guangdong(self):
        """广东普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '4400163320', 'fphm': '00021010', 'jym': '005051','kprq': '20180102','uniqueId':'1000004',
            'sign':md5("fpdm=4400163320&fphm=00021010&fplx=04&jym=005051&kprq=20180102&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def guangxi(self):
        """广西普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '4500172320', 'fphm': '09251966', 'jym': '849993',
                   'kprq': '20180105','uniqueId':'1000004',
                   'sign':md5("fpdm=4500172320&fphm=09251966&fplx=04&jym=849993&kprq=20180105&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def hainan(self):
        """海南普通发票查验"""
        payload = {'fplx': '01', 'fpdm': '4600163130', 'fphm': '01208520',
                   'fpje': '816610.26','kprq': '20171123','uniqueId':'1000004',
                   'sign':md5("fpdm=4600163130&fphm=01208520&fpje=816610.26&fplx=01&kprq=20171123&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def shaxi(self):
        """陕西普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '6100171320', 'fphm': '09030275',  'jym': '911427',
                   'kprq': '20170626','uniqueId':'1000004',
                   'sign':md5("fpdm=6100171320&fphm=09030275&fplx=04&jym=911427&kprq=20170626&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def yunnan(self):
        """云南普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '5300171320', 'fphm': '13826269', 'jym': '578163',
                    'kprq': '20171119', 'uniqueId': '1000004',
                    'sign': md5("fpdm=5300171320&fphm=13826269&fplx=04&jym=578163&kprq=20171119&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def heilongjiang(self):
        """黑龙江普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '2300173320', 'fphm': '12299469', 'jym': '239171',
                    'kprq': '20180203', 'uniqueId': '1000004',
                    'sign': md5("fpdm=2300173320&fphm=12299469&fplx=04&jym=239171&kprq=20180203&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def guizhou(self):
        """贵州普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '5200173320', 'fphm': '07708742', 'jym': '407547',
                    'kprq': '20180127', 'uniqueId': '1000004',
                    'sign': md5("fpdm=5200173320&fphm=07708742&fplx=04&jym=407547&kprq=20180127&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def xizang(self):
        """西藏普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '5400171320', 'fphm': '01316456', 'jym': '536623',
                    'kprq': '20171209', 'uniqueId': '1000004',
                    'sign': md5("fpdm=5400171320&fphm=01316456&fplx=04&jym=536623&kprq=20171209&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def gansu(self):
        """甘肃普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6200171350', 'fphm': '00324121', 'jym': '376901',
                    'kprq': '20180227', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6200171350&fphm=00324121&fplx=04&jym=376901&kprq=20180227&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def qinghai(self):
        """青海普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6300162350', 'fphm': '02226976', 'jym': '163565',
                    'kprq': '20180113', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6300162350&fphm=02226976&fplx=04&jym=163565&kprq=20180113&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def ningxi(self):
        """宁夏普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6400173320', 'fphm': '02748815', 'jym': '197261',
                    'kprq': '20180323', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6400173320&fphm=02748815&fplx=04&jym=197261&kprq=20180323&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload

    def xinjiang(self):
        """新疆普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6500174320', 'fphm': '04312540', 'jym': '393788',
                    'kprq': '20180111', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6500174320&fphm=04312540&fplx=04&jym=393788&kprq=20180111&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        return payload
