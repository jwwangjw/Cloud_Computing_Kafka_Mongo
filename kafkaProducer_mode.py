import csv
from kafka import KafkaProducer
import time

def main():
    ##生产模块
    producer = KafkaProducer(bootstrap_servers=['url'])
    with open('D:/QQfile/answer_results.csv','r',encoding='utf8')as fp:
        reader=csv.reader(fp)
        data_temp=[]
        for row in reader:
            data_temp.append(row)
        date=[]
        pos=0
        while (pos<len(data_temp)-1):
            pre = []
            pre.append(data_temp[pos][0])
            temp=0
            for i in range(pos,len(data_temp)-1):
                if data_temp[i][0]==data_temp[i+1][0]:
                    date=data_temp[i][0]
                    pre.append(data_temp[i][1])
                else:
                    temp=i+1
                    break
            print(temp)
            pos=temp
            print(pos)
            if(len(pre)!=1):
                for j in range(len(pre)):
                    string=pre[j]
                    producer.send("txt", bytes(string.replace('\n','').encode('utf-8')))
                    print(bytes(string.replace('\n','').encode('utf-8')))
                print(pre)
            time.sleep(5)
if __name__ == '__main__':
    main()
