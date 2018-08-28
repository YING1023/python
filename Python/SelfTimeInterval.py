import time

def TimeInterval(interval):
    try:
        #time_remaining = interval - time.time() % interval
        print("[%s] %s"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "start"))
        time.sleep(interval)
        print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "stop"))
    except:
        print("错误")

def main():
    interval=5
    for i in range(6):
        print(i)
        TimeInterval(interval)

main()