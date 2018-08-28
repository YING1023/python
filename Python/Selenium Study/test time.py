import time
def Timeinterval(interval):
    try:
        time_remaining = interval
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "start"))
        time.sleep(time_remaining)
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "stop"))
    except:
        print("错误")

def main():
    Timeinterval(5)
    print("[%s] %s" %(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()),"To be continued"))

main()
