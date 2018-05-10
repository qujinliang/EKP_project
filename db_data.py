from pymongo import MongoClient
import re
import time

client = MongoClient('',)
db = client.user
db.authenticate("","")
db = client.user
collection = db.fc_invoice_info

fp_list2 = ['87120411','58929139','00271772','11695353','19768327','06001047','66718525','02062714','11610387',
			'01875257','05331852','50657158','06998169','22052218','47982351','02188236','00021010','09251966',
			'01208520','09030275','13826269','12299469','07708742','01316456','00324121','02226976','02748815',
			'04312540','15967293']
time.sleep(30)

for i in fp_list2:
	collection.remove({'fphm':i})
