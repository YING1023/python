try:
    path='G:\Python\cet4\cet4.txt'
    f = open(path,'r')#测试文件是否打开成功
    f.read()
    f.close()
    #用with代替f.close（）
    list =[]
    with open(path,'r') as f:
        for line in f.readlines():
            list.append(line.strip('\n'))#用strip去掉结尾的\n
    for date in list:
        print(date)

except:
    print('错误')