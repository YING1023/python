'''try:
    path='G:\Python\cet4\cet4.txt'
    f=open(path,'r')
    f.read()
    f.close()
    list=[]

    with open(path,'r') as f:
        
        for line in f.readlines():
            list.append(line.strip('\n'))

    for n in list:
        print(n)

except:
    print("worry") 

import time


def IntervalTime(intervalTime):

    try:
        print("[%s],%s"%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),"stop"))
        time.sleep(intervalTime)
        print("[%s],%s"%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),"start"))


    except:
        print("timeworry")


def main():
    
    interval=5
    for n in  range(6):
        print(n)
        IntervalTime(interval)

main() '''









