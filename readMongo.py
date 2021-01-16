import pandas as pd
import matplotlib.pyplot as plt
import pymongo
# 连接mongodb数据库
client = pymongo.MongoClient('mongodb://admin:admin@119.23.222.7:27017')
# 连接数据库
db = client["zhihu"]
# 数据表
dataB = db["test"]
data = pd.DataFrame(list(dataB.find()))
data.head()
data.to_csv('szHousePrice.csv',encoding='utf-8')