# -*- coding:UTF-8 -*-

import time
import hashlib

# 长软接口用户名
USER_NAME = "banguser"
# 长软接口密码
USER_PWD = "bangong@)!^"

fplx = "04"
fpdm = "3100162320"
fphm = "56618159"
jym  = "690593"
kprq = "20170213"
uniqueId = "1000004"
privet  = "de92dbf0b12d11e6aa28b0c090607876"
send_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
md5str = fplx+fpdm+fphm+jym+kprq+uniqueId+privet

# paixu = ["fpdm=4400161320","fphm=01304449","fplx=04","fpje=633.96","kprq=20170813"]
# print(sorted(paixu))

def md5(md5_str):
    m2 = hashlib.md5()
    m2.update(md5_str)
    return m2.hexdigest()
# print(md5("fpdm=4400161320&fphm=01304449&fplx=04&jym=271854&kprq=20180126&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8")))
#print(md5("fpdm=3600163130&fphm=06998169&fpje=1522.64&fplx=01&kprq=20171018&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8")))
