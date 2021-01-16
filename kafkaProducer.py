import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import time


def main():
    ##生产模块
    producer = KafkaProducer(bootstrap_servers=['url'])
    with open('D:\QQfile\separateWord_day.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)
        items = json_data.items()
        keys = []
        for key, value in items:
            keys.append(str(key))
        print(keys)
        for i in range(len(keys)):
            producer.send("txt", bytes(keys[i].encode('utf-8')))
            string=str(json_data[keys[i]])
            producer.send("txt", bytes(string.replace('\n','').encode('utf-8')))
            print(bytes(string.replace('\n','').encode('utf-8')))
            time.sleep(5)
if __name__ == '__main__':
    main()
