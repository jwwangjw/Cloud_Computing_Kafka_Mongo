from pymongo import *
import json


class JsonToMongo(object):
    def __open_file(self):
        self.file = open('result_mode.json', 'r')
        # 创建mongodb客户端
        self.client = MongoClient('url')
        # 创建数据库
        self.db = self.client.zhihu
        # 创建集合
        self.collection = self.db.mode

    # 关闭文件
    def __close_file(self):
        self.file.close()

    # 写入数据库
    def write_database(self):
        self.__open_file()

        # 转换为python对象
        data = json.load(self.file)

        try:
            self.collection.insert(data)
            print('写入成功')
        except Exception as e:
            print(e)
        finally:
            self.__close_file()


if __name__ == '__main__':
    j2m = JsonToMongo()
    j2m.write_database()
