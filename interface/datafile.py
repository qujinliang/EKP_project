from interface.jiami import *

'''发票数据存储模块'''

class DataFile():

    def tianjin(self):
        """天津普通发票查验"""
        # 发送时间
        send_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        # 发票数据
        payload = {
            "fpdm": "012001800111", "fphm": "28342319", "fplx": "10", "jym": "305143", "kprq": "20180702"
        }
        # 拼接MD5加密串
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
           "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (payload['fplx'],payload['fpdm'],payload['fphm'],  payload['kprq'],payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>"% (request_xml, USER_NAME, send_time,md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def shanghai(self):
        """上海普通发票查验"""
        payload = {
            "fpdm": "031001800104","fphm": "32078777","fplx": "10","jym": "520141","kprq": "20180702","uniqueId": "1000004"
        }
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def beijing(self):
        """北京普通发票查验"""
        payload = {
            "fpdm": "011001800104","fphm": "00078024","fplx": "04","jym": "390276","kprq": "20180702","uniqueId": "1000004",
            "sign":md5("fpdm=1100173320&fphm=58929139&fplx=04&jym=056970&kprq=20180103&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def hebei(self):
        """河北普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '013001800104', 'fphm': '15770352', 'jym': '107486', 'kprq': '20180704','uniqueId': '1000004',
            'sign': md5("fpdm=1300171320&fphm=00271772&fplx=04&jym=936815&kprq=20170927&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def liaoning(self):
        """辽宁普通发票查验成功"""
        payload = {
            'fplx': '04', 'fpdm': '2100172350', 'fphm': '03656686', 'jym': '544362', 'kprq': '20180703','uniqueId': '1000004',
            'sign': md5("fpdm=2100171320&fphm=11695353&fplx=04&jym=893273&kprq=20170925&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def anhui(self):
        """安徽普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '034001800104', 'fphm': '03176421','jym': '743609','kprq': '20180703','uniqueId':'1000004',
                   'sign':md5("fpdm=3400172320&fphm=19768327&fplx=04&jym=156228&kprq=20171020&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def henan(self):
        """河南普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '041001800104', 'fphm': '33664210', 'jym': '546161','kprq': '20180704', 'uniqueId': '1000004',
            'sign': md5("fpdm=4100173320&fphm=06001047&fplx=04&jym=489592&kprq=20180105&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def shenzhen(self):
        """深圳普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '4400173320', 'fphm': '52517331',  'jym': '479256','kprq': '20180703','uniqueId':'1000004',
                   'sign':md5("fpdm=4403162320&fphm=66718525&fplx=04&jym=520590&kprq=20170814&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def shanxi(self):
        """山西普通发票查验成功"""
        payload = {
            'fplx': '04', 'fpdm': '1400174320', 'fphm': '05907842', 'jym': '634803','kprq': '20180705','uniqueId':'1000004',
            'sign':md5("fpdm=1400171130&fphm=02062714&fpje=17094.03&fplx=01&kprq=20171117&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def neimeng(self):
        """内蒙普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '1500164320', 'fphm': '05361818', 'jym': '914642','kprq': '20180704','uniqueId':'1000004',
            'sign':md5("fpdm=1500171320&fphm=11610387&fplx=04&jym=496101&kprq=20180113&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def jilin(self):
        """吉林普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '2200172320', 'fphm': '05724734', 'jym': '517491','kprq': '20180703','uniqueId':'1000004',
            'sign':md5("fpdm=2200162350&fphm=01875257&fplx=04&jym=878078&kprq=20171115&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def zhejiang(self):
        """浙江专用发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '3300174320', 'fphm': '13281859',  'jym': '719842','kprq': '20180703','uniqueId':'1000004',
            'sign':md5("fpdm=3300154130&fphm=05331852&fpje=53.68&fplx=01&kprq=20171010&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def fujian(self):
        """福建普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '3500172320', 'fphm': '00769315', 'jym': '880634','kprq': '20180702','uniqueId':'1000004',
            'sign':md5("fpdm=3500163320&fphm=50657158&fplx=04&jym=912642&kprq=20180102&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def jiangxi(self):
        """江西普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '3600162350', 'fphm': '04593132', 'jym': '607628','kprq': '20180702','uniqueId':'1000004',
            'sign':md5("fpdm=3600163130&fphm=06998169&fpje=1522.64&fplx=01&kprq=20171018&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def shandong(self):
        """山东普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '3700162350', 'fphm': '29345619', 'jym': '357679','kprq': '20180702','uniqueId':'1000004',
            'sign':md5("fpdm=3700171320&fphm=22052218&fplx=04&jym=728827&kprq=20180105&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param
    def hubei(self):
        """湖北普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '4200171320', 'fphm': '38802164', 'jym': '799470','kprq': '20180702','uniqueId':'1000004',
            'sign':md5("fpdm=4200164320&fphm=47982351&fplx=04&jym=464625&kprq=20171026&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def hunan(self):
        """湖南普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '043001800104', 'fphm': '19084019', 'jym': '232329','kprq': '20180702','uniqueId':'1000004',
            'sign':md5("fpdm=4300173320&fphm=02188236&fplx=04&jym=883431&kprq=20180103&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def guangdong(self):
        """广东普通发票查验"""
        payload = {
            'fplx': '04', 'fpdm': '4400173320', 'fphm': '52517331', 'jym': '479256','kprq': '20180703','uniqueId':'1000004',
            'sign':md5("fpdm=4400163320&fphm=00021010&fplx=04&jym=005051&kprq=20180102&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def guangxi(self):
        """广西普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '4500173320', 'fphm': '01143203', 'jym': '861570',
                   'kprq': '20180702','uniqueId':'1000004',
                   'sign':md5("fpdm=4500172320&fphm=09251966&fplx=04&jym=849993&kprq=20180105&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def hainan(self):
        """海南普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '4600171320', 'fphm': '00502207',
                   'jym': '797949','kprq': '20180704','uniqueId':'1000004',
                   'sign':md5("fpdm=4600163130&fphm=01208520&fpje=816610.26&fplx=01&kprq=20171123&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def shaxi(self):
        """陕西普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '6100173320', 'fphm': '30969125',  'jym': '348087',
                   'kprq': '20180706','uniqueId':'1000004',
                   'sign':md5("fpdm=6100171320&fphm=09030275&fplx=04&jym=911427&kprq=20170626&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def yunnan(self):
        """云南普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '5300173320', 'fphm': '02334639', 'jym': '929554',
                    'kprq': '20180703', 'uniqueId': '1000004',
                    'sign': md5("fpdm=5300171320&fphm=13826269&fplx=04&jym=578163&kprq=20171119&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def heilongjiang(self):
        """黑龙江普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '2300173320', 'fphm': '03551408', 'jym': '208020',
                    'kprq': '20180704', 'uniqueId': '1000004',
                    'sign': md5("fpdm=2300173320&fphm=12299469&fplx=04&jym=239171&kprq=20180203&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def guizhou(self):
        """贵州普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '052001800104', 'fphm': '08968244', 'jym': '416778',
                    'kprq': '20180708', 'uniqueId': '1000004',
                    'sign': md5("fpdm=5200173320&fphm=07708742&fplx=04&jym=407547&kprq=20180127&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def xizang(self):
        """西藏普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '054001800105', 'fphm': '00277985', 'jym': '624967',
                    'kprq': '20180706', 'uniqueId': '1000004',
                    'sign': md5("fpdm=5400171320&fphm=01316456&fplx=04&jym=536623&kprq=20171209&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def gansu(self):
        """甘肃普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6200172320', 'fphm': '07739962', 'jym': '185518',
                    'kprq': '20180704', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6200171350&fphm=00324121&fplx=04&jym=376901&kprq=20180227&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def qinghai(self):
        """青海普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '063001800105', 'fphm': '00068890', 'jym': '692286',
                    'kprq': '20180702', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6300162350&fphm=02226976&fplx=04&jym=163565&kprq=20180113&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def ningxi(self):
        """宁夏普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6400171320', 'fphm': '05119302', 'jym': '992667',
                    'kprq': '20180708', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6400173320&fphm=02748815&fplx=04&jym=197261&kprq=20180323&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def xinjiang(self):
        """新疆普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '6500174320', 'fphm': '12603874', 'jym': '707615',
                    'kprq': '20180702', 'uniqueId': '1000004',
                    'sign': md5("fpdm=6500174320&fphm=04312540&fplx=04&jym=393788&kprq=20180111&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def jiangsu(self):
        """江苏普通发票查验`"""
        payload = {'fplx': '04', 'fpdm': '3200154320', 'fphm': '18866763', 'jym': '146902',
                    'kprq': '20180702', 'uniqueId': '1000004',
                    'sign': md5("fpdm=3200154320&fphm=15967293&fplx=04&jym=497112&kprq=20180104&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param

    def chongqing(self):
        """重庆普通发票查验"""
        payload = {'fplx': '04', 'fpdm': '5000174320', 'fphm': '17459349',
                   'jym': '725686','kprq': '20180702','uniqueId':'1000004',
                   'sign':md5("fpdm=5000181130&fphm=01035487&fpje=5490.57&fplx=01&kprq=20180314&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))}
        md5str = USER_NAME + payload['fpdm'] + payload['fphm'] + send_time + USER_PWD
        # 拼接request xml串
        request_xml = "<FPLX>%s</FPLX><FPDM>%s</FPDM><FPHM>%s</FPHM>" \
                      "<KPRQ>%s</KPRQ><JYM>%s</JYM>" % (
                      payload['fplx'], payload['fpdm'], payload['fphm'], payload['kprq'], payload['jym'])

        invoice_info_param = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><MSG><VERSION>2</VERSION>%s<USERNAME>%s</USERNAME><SENDTIME>%s</SENDTIME><SIGN>%s</SIGN></MSG>" % (
        request_xml, USER_NAME, send_time, md5(md5str.encode("utf-8")))
        # print("datafile=" + invoice_info_param)
        return invoice_info_param
