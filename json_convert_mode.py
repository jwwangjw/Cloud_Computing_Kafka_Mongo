import json
import os

all_files=[]
filename='C:/Users/lenovo/Desktop/2020-01-20.txt'
for root, dirs, files in os.walk(r"D:\test\wordcount"):
    for dir in dirs:
        all_files.append(os.path.join(root, dir))
dict_all={}
for i in range(len(all_files)):
    filename=all_files[i]+'\part-00000'
    with open(filename, 'r',encoding='UTF-8') as fp:
        lines = fp.readlines()
        if(len(lines)!=0):
            day=lines[0].split(',')[0].replace('(','').replace('\'','')
            dict_day={}
            key=[]
            value=[]
            for j in range(1,len(lines)):
                line=lines[j]
                list=[]
                line=line.replace('(','').replace(')','').replace('\n','').replace('\'','').replace('）','')
                list=line.split(',')
                for n in range(len(list)):
                    list[n]=list[n].strip()
                if list[0]=='0':
                    list[0]='neutral'
                elif list[0]=='1':
                    list[0]='postive'
                else:
                    list[0]='negative'
                key.append(list[0])
                value.append(list[1])
            if 'neutral' not in key:
                key.append('neutral')
                value.append(0)
            if 'postive' not in key:
                key.append('postive')
                value.append(0)
            if 'negative' not in key:
                key.append('negative')
                value.append(0)
            for m in range(len(key)):
                dict_day[str(key[m])]=int(value[m])
            dict_all[day]=dict_day
with open("result_mode.json", "w") as fp:
    fp.write(json.dumps(dict_all,indent=4))